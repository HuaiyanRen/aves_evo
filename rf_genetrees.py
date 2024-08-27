from ete3 import Tree
import os
import csv 

result_folder = 'mix_c12/'
with open('nrf_mix_c12.csv','w+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    csv_write.writerow(['name', 'nrf_main', 'nrf_gene', 'nrf_ref'])

with open("14972_exon_alns_namelist.txt") as f:
    f_list = f.readlines()

main_treefile = '63K_abb.treefile'

for i in range(0,200):
    gene_treefile = 'gene_trees/' + f_list[i].split(" ")[1].split('.')[0] + '.treefile'
    mf_treefile = result_folder +str(i) + '_'+ f_list[i].split(" ")[1].split('.')[0] + '.treefile'    
    pruned_treefile = result_folder +str(i) + '_'+f_list[i].split(" ")[1].split('.')[0] + '_main_pruned.treefile'
    pruned_treefile_g = result_folder +str(i) + '_'+f_list[i].split(" ")[1].split('.')[0] + '_gene_pruned.treefile'
    

    if not os.path.isfile(pruned_treefile):
        gene_treestr = open(mf_treefile,'r').read()
        gene_tree = Tree(gene_treestr)
        taxa = set(gene_tree.get_leaf_names())
        
        species_treestr = open(main_treefile,'r').read()
        species_tree = Tree(species_treestr,format=1)
        species_tree.prune(taxa)
        species_tree.unroot()

        with open(pruned_treefile, 'w+') as result:
            result.write(species_tree.write() + '\n')
            
    if not os.path.isfile(pruned_treefile_g):
        gene_treestr = open(mf_treefile,'r').read()
        gene_tree = Tree(gene_treestr)
        taxa = set(gene_tree.get_leaf_names())
        
        species_treestr = open(gene_treefile,'r').read()
        species_tree = Tree(species_treestr,format=1)
        species_tree.prune(taxa)
        species_tree.unroot()

        with open(pruned_treefile_g, 'w+') as result:
            result.write(species_tree.write() + '\n')
        
    if not os.path.isfile(result_folder + str(i) + '_'+ f_list[i].split(" ")[1].split('.')[0] + '_rfmain.rfdist'):
        cmd = '/data/huaiyan/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -rf ' + pruned_treefile + ' ' + mf_treefile + ' -redo -pre ' + result_folder + str(i) + '_'+ f_list[i].split(" ")[1].split('.')[0] + '_rfmain'
        os.system(cmd)
    
    if not os.path.isfile(result_folder + str(i) + '_'+ f_list[i].split(" ")[1].split('.')[0] + '_rfgene.rfdist'):
    cmd = '/data/huaiyan/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -rf ' + pruned_treefile_g + ' ' + mf_treefile + ' -redo -pre ' + result_folder + str(i) + '_'+ f_list[i].split(" ")[1].split('.')[0] + '_rfgene'
    os.system(cmd)
        
    if not os.path.isfile(result_folder + str(i) + '_'+ f_list[i].split(" ")[1].split('.')[0] + '_rfref.rfdist'):
    cmd = '/data/huaiyan/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -rf ' + pruned_treefile_g + ' ' + pruned_treefile + ' -redo -pre ' + result_folder + str(i) + '_'+ f_list[i].split(" ")[1].split('.')[0] + '_rfref'
    os.system(cmd)

    with open(result_folder +str(i) + '_'+ f_list[i].split(" ")[1].split('.')[0] + '.iqtree') as iq_f:
        for line in iq_f.readlines():
            if 'Input data: ' in line:
                ntaxa = float(line.split()[-6])
                
    with open(result_folder + str(i) + '_'+ f_list[i].split(" ")[1].split('.')[0] + '_rfmain.rfdist') as b:
        for line in b.readlines():
            if 'Tree0' in line:
                nrfmain = float(line.split()[-1])/(2*ntaxa-6)
                
    with open(result_folder + str(i) + '_'+ f_list[i].split(" ")[1].split('.')[0] + '_rfgene.rfdist') as b:
        for line in b.readlines():
            if 'Tree0' in line:
                nrfgene = float(line.split()[-1])/(2*ntaxa-6)

    with open(result_folder + str(i) + '_'+ f_list[i].split(" ")[1].split('.')[0] + '_rfref.rfdist') as b:
        for line in b.readlines():
            if 'Tree0' in line:
                nrfref = float(line.split()[-1])/(2*ntaxa-6)

    result_row = [f_list[i].split(" ")[1].split('.')[0], nrfmain, nrfgene, nrfref]
 
    with open('nrf_mix_c12.csv','a+',newline='') as csvf:
        csv_write = csv.writer(csvf)
        csv_write.writerow(result_row) 
