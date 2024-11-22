from multiprocessing import Pool
from functools import partial
import os
import subprocess


with open("exon_namelist_random.txt") as f:
    f_list = f.readlines()

def run_i(i):   
    
    name = f_list[i].split(" ")[1].rstrip()    
    
    if not os.path.isfile('rf_compare/'+str(i) + '_' + name + '_rf.rfdist'):
        candi_treefile1 = 'sin_c12/'+str(i) + '_' + name + '.treefile'
        candi_treefile2 = 'mix_c12/'+str(i) + '_' + name + '.treefile'
        
        if os.path.isfile('sin_c12/'+str(i) + '_' + name + '.uniqueseq.phy'):
                
            candi_treefile1 = 'sin_c12/'+str(i) + '_' + name + '_unique.treefile'
            candi_treefile2 = 'mix_c12/'+str(i) + '_' + name + '_unique.treefile'
    
        
        cmd = '/home/huaiyan/software/iqtree-2.3.6.6.mf-Linux-intel/bin/iqtree2 -rf ' + candi_treefile1 + ' ' + candi_treefile2 + ' -redo -pre rf_compare/'+str(i) + '_' + name + '_rf'
        os.system(cmd)

    if not os.path.isfile('rf_compare/'+str(i) + '_' + name + '_pythia.txt'):

        cmdp = 'pythia --msa c12/' + name + '.cds.fa --raxmlng /home/huaiyan/software/raxml-ng --removeDuplicates'

        result = subprocess.run(cmdp, shell=True, text=True, capture_output=True)
        with open('rf_compare/'+str(i) + '_' + name + '_pythia.txt', 'w+') as f:
            f.write(result.stdout)
            f.write(result.stderr)
            
i_list = list(range(0,1000,1))

partial_running = partial(run_i)

with Pool(20) as p:
    score_list = p.map(partial_running, i_list) 
            