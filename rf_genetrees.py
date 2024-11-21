from multiprocessing import Pool
from functools import partial
import os
import numpy as np
from ete3 import Tree
import csv

with open("exon_namelist_random.txt") as f:
    f_list = f.readlines()


# =============================================================================
# result_csv = 'rf_' +  result_folder + '.csv'
# with open(result_csv,'w+',newline='') as csvf:
#     csv_write = csv.writer(csvf)
#     csv_write.writerow(['name', 'model', 
#                         'rf_main', 'rf_exon', 'rf_gene',
#                         'nrf_main', 'nrf_exon', 'nrf_gene'])
# 
# with open(folder + '/'+str(i) + '_' + name + '.iqtree') as iq_f:
#     for line in iq_f.readlines():
#         if 'Input data: ' in line:
#             ntaxa = float(line.split()[-6])
#             
# with open(folder + '/'+str(i) + '_' + name + '_rfmain.rfdist') as b:
#     for line in b.readlines():
#         if 'Tree0' in line:
#             rfmain = float(line.split()[-1])
#             nrfmain = rfmain/(2*ntaxa-6)
#             
# with open(folder + '/'+str(i) + '_' + name + '_rfexon.rfdist') as b:
#     for line in b.readlines():
#         if 'Tree0' in line:
#             rfexon = float(line.split()[-1])
#             nrfexon = rfexon/(2*ntaxa-6)
# 
# with open(folder + '/'+str(i) + '_' + name + '_rfgene.rfdist') as b:
#     for line in b.readlines():
#         if 'Tree0' in line:
#             rfgene = float(line.split()[-1])
#             nrfgene = rfgene/(2*ntaxa-6)
# 
# result_row = [name, folder,
#               rfmain, rfexon, rfgene,
#               nrfmain, nrfexon, nrfgene]
# 
# with open(result_csv','a+',newline='') as csvf:
#     csv_write = csv.writer(csvf)
#     csv_write.writerow(result_row) 
# =============================================================================


main_treefile = 'main_abb_unrooted.treefile'
exon_treefile = 'exon_unrooted.treefile'

def read_phylip(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    sequence_names = []
    for line in lines[1:]:
        line = line.strip()
        name = line.split()[0]
        sequence_names.append(name)
    return set(sequence_names)


def run_rf(tuple_list):   
    folder, i = tuple_list
    
    name = f_list[i].split(" ")[1].rstrip()    
    candi_treefile = folder + '/'+str(i) + '_' + name + '.treefile' 
    gene_treefile = 'exon_trees/' + name + '.treefile'   
    pruned_m_treefile = folder + '/'+str(i) + '_' + name + '_main_pruned.treefile'
    pruned_e_treefile = folder + '/'+str(i) + '_' + name + '_exon_pruned.treefile'
    
    
    if not os.path.isfile(folder + '/'+str(i) + '_' + name + '.uniqueseq.phy'):
        gene_treestr = open(candi_treefile,'r').read()
        gene_tree = Tree(gene_treestr)
        taxa = set(gene_tree.get_leaf_names())
    else:
        taxa = read_phylip(folder + '/'+str(i) + '_' + name + '.uniqueseq.phy')
        
        species_treestr = open(candi_treefile,'r').read()
        species_tree = Tree(species_treestr,format=1)
        species_tree.prune(taxa)
        species_tree.unroot()

        with open(folder + '/'+str(i) + '_' + name + '_unique.treefile', 'w+') as result:
            result.write(species_tree.write() + '\n')
        candi_treefile = folder + '/'+str(i) + '_' + name + '_unique.treefile'  

        species_treestr = open(gene_treefile,'r').read()
        species_tree = Tree(species_treestr,format=1)
        species_tree.prune(taxa)
        species_tree.unroot()

        with open(folder + '/'+str(i) + '_' + name+ '_uniqueexon.treefile', 'w+') as result:
            result.write(species_tree.write() + '\n')
        gene_treefile = folder + '/'+str(i) + '_' + name +  '_uniqueexon.treefile'         

    if not os.path.isfile(pruned_m_treefile):        
        
        species_treestr = open(main_treefile,'r').read()
        species_tree = Tree(species_treestr,format=1)
        species_tree.prune(taxa)
        species_tree.unroot()

        with open(pruned_m_treefile, 'w+') as result:
            result.write(species_tree.write() + '\n')
            
    if not os.path.isfile(pruned_e_treefile):

        species_treestr = open(exon_treefile,'r').read()
        species_tree = Tree(species_treestr,format=1)
        species_tree.prune(taxa)
        species_tree.unroot()

        with open(pruned_e_treefile, 'w+') as result:
            result.write(species_tree.write() + '\n')
        
    if not os.path.isfile(folder + '/'+str(i) + '_' + name + '_rfmain.rfdist'):
        cmd = '/home/huaiyan/software/iqtree-2.3.6.6.mf-Linux-intel/bin/iqtree2 -rf ' + candi_treefile + ' ' + pruned_m_treefile + ' -redo -pre ' + folder + '/'+str(i) + '_' + name + '_rfmain'
        os.system(cmd)
    
    if not os.path.isfile(folder + '/'+str(i) + '_' + name + '_rfexon.rfdist'):
        cmd = '/home/huaiyan/software/iqtree-2.3.6.6.mf-Linux-intel/bin/iqtree2 -rf ' + candi_treefile + ' ' + pruned_e_treefile + ' -redo -pre ' + folder + '/'+str(i) + '_' + name + '_rfexon'
        os.system(cmd)
        
    if not os.path.isfile(folder + '/'+str(i) + '_' + name + '_rfgene.rfdist'):
        cmd = '/home/huaiyan/software/iqtree-2.3.6.6.mf-Linux-intel/bin/iqtree2 -rf ' + candi_treefile + ' ' + gene_treefile + ' -redo -pre ' + folder + '/'+str(i) + '_' + name + '_rfgene'
        os.system(cmd)

i_list = list(range(0,1000,1))
result_folder = 'sin_c12'
tuple_list = ['']*len(i_list)

for i in range(len(tuple_list)):
    tuple_list[i] = result_folder, i_list[i]

partial_running = partial(run_rf)

with Pool(50) as p:
    score_list = p.map(partial_running, tuple_list)   
