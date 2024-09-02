from multiprocessing import Pool
from functools import partial
import subprocess
import numpy as np
import argparse
import sys
import os


# =============================================================================
# import os
# file_names = os.listdir("14972_exon_alns")
# #file_names = [f for f in os.listdir("/14972_exon_alns") if os.path.isfile(os.path.join("/14972_exon_alns", f))]
# 
# file_names = sorted(file_names)
# 
# with open("14972_exon_alns_namelist.txt", 'w') as f:
#     i = 0
#     for file_name in file_names:
#         if file_name[0] != ".":
#             f.write(f"{i} {file_name}\n")
#             i+= 1
# =============================================================================


with open("14972_exon_alns_namelist.txt") as f:
    f_list = f.readlines()

def run_mix123(tuple_list):   
    model, i = tuple_list
    f_name = 'c123/'+ f_list[i].split(" ")[1].split('.')[0] + '.cds.fa'
    out_name = 'mix_c123/'+str(i) + '_' + f_list[i].split(" ")[1].split('.')[0]


    cmd1 = '/usr/bin/time -v /data/huaiyan/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m MIX+MFP -mset GTR -mrate E,I,G,I+G,R,I+R -wspm -qmax 20 -pre '+out_name+ ' -nt 1 -s '+f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'w') as f:
        #f.write(result.stdout)
        f.write(result.stderr)
        
def run_mix12(tuple_list):      
    model, i = tuple_list 
    f_name = 'c12/'+ f_list[i].split(" ")[1].split('.')[0] + '.cds.fa'
    out_name = 'mix_c12/'+str(i) + '_' + f_list[i].split(" ")[1].split('.')[0]

    cmd1 = '/usr/bin/time -v /data/huaiyan/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m MIX+MFP -mset GTR -mrate E,I,G,I+G,R,I+R -wspm -qmax 20 -pre '+out_name+ ' -nt 1 -s '+f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'w') as f:
        #f.write(result.stdout)
        f.write(result.stderr)        

def run_part123(tuple_list):   
    model, i = tuple_list
    f_name = 'c123/'+ f_list[i].split(" ")[1].split('.')[0] + '.cds.fa'
    out_name = 'part_c123/'+str(i) + '_' + f_list[i].split(" ")[1].split('.')[0]

    part_name = 'c123/'+ f_list[i].split(" ")[1].split('.')[0] + '_part.nex'
    if not os.path.isfile(part_name):
        amas_cmd = 'python3 AMAS.py concat -f fasta -d dna -i ' + f_name + ' -u fasta -p ' + part_name + ' -n 123 --part-format nexus -t ' + f_name
        os.system(amas_cmd)

    cmd1 = '/usr/bin/time -v /scratch/dx61/hr8997/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m MFP+MERGE -mset GTR -mfreq FO -pre '+out_name+ ' -nt 1 -s '+f_name + ' -p '+part_name
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'w') as f:
        #f.write(result.stdout)
        f.write(result.stderr)
        
def run_part12(tuple_list):      
    model, i = tuple_list 
    f_name = 'c12/'+ f_list[i].split(" ")[1].split('.')[0] + '.cds.fa'
    out_name = 'part_c12/'+str(i) + '_' + f_list[i].split(" ")[1].split('.')[0]

    part_name = 'c12/'+ f_list[i].split(" ")[1].split('.')[0] + '_part.nex'
    if not os.path.isfile(part_name):
        amas_cmd = 'python3 AMAS.py concat -f fasta -d dna -i ' + f_name + ' -u fasta -p ' + part_name + ' -n 12 --part-format nexus -t ' + f_name
        os.system(amas_cmd)

    cmd1 = '/usr/bin/time -v /scratch/dx61/hr8997/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m MFP+MERGE -mset GTR -mfreq FO -pre '+out_name+ ' -nt 1 -s '+f_name + ' -p '+part_name
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'w') as f:
        #f.write(result.stdout)
        f.write(result.stderr)  

def run_aa(tuple_list):     
    model, i = tuple_list
    f_name = 'pep/'+ f_list[i].split(" ")[1].split('.')[0] + '.pep.fa'
    out_name = 'aa/'+str(i) + '_' + f_list[i].split(" ")[1].split('.')[0]

    cmd1 = '/usr/bin/time -v /scratch/dx61/hr8997/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m MFP -mset Q.bird -mrate E,I,G,I+G,R,I+R -pre '+out_name+ ' -nt 1 -s '+f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'w') as f:
        #f.write(result.stdout)
        f.write(result.stderr)
 
def run_aa_c20(tuple_list):     
    model, i = tuple_list  
    f_name = 'pep/'+ f_list[i].split(" ")[1].split('.')[0] + '.pep.fa'
    out_name = 'aa/'+str(i) + '_' + f_list[i].split(" ")[1].split('.')[0]
    out_name_c20 = 'aa_c20/'+str(i) + '_' + f_list[i].split(" ")[1].split('.')[0]
    
# =============================================================================
#     if os.path.isfile(out_name + '.iqtree'):
#         if not os.path.isfile(out_name_c20 + '.iqtree'):
#             rhas = ''
#             with open(out_name + '.iqtree') as f:
#                 for line in f.readlines():
#                     if 'Best-fit model according to BIC: ' in line:
#                         if '+F' in line:
#                             rhas = line.split('+F')[-1].rstrip('\n') 
#                         else:
#                             rhas = line.split('Q.bird')[-1].rstrip('\n') 
#     
#             cmd1 = '/usr/bin/time -v /scratch/dx61/hr8997/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m Q.bird+C20' + rhas + ' -pre '+out_name_c20+ ' -nt 3 -s '+f_name 
#             result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
#             with open(out_name_c20 + '_time.txt', 'w') as f:
#                 #f.write(result.stdout)
#                 f.write(result.stderr)
#     else:
#         print(out_name + '.iqtree does not exist')
# =============================================================================
        
    cmd1 = '/usr/bin/time -v /scratch/dx61/hr8997/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m Q.bird+C20+I+G -pre '+out_name_c20+ ' -nt 3 -s '+f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name_c20 + '_time.txt', 'w') as f:
        #f.write(result.stdout)
        f.write(result.stderr)

# 14972
def control(model, start, end, n_pool):
    if model not in ['mix123', 'mix12', 'aa', 'aa_c20', 'part123', 'part12']:
        print("wrong model type")
        sys.exit(1)
           
    start = int(start)
    end = int(end)
    n_pool = int(n_pool)
    if model == 'aa_c20':
        n_pool = int(n_pool/3)
    
    replicates = list(np.arange(start,end,1))
    
    tuple_list = ['']*len(replicates)

    for i in range(len(tuple_list)):
        tuple_list[i] = model, replicates[i]
        
    if model == 'mix123':
        partial_running = partial(run_mix123)
    elif model == 'mix12':
        partial_running = partial(run_mix12)
    elif model == 'part123':
        partial_running = partial(run_part123)
    elif model == 'part12':
        partial_running = partial(run_part12)
    elif model == 'aa':
        partial_running = partial(run_aa)
    elif model == 'aa_c20':
        partial_running = partial(run_aa_c20)   
        
    with Pool(n_pool) as p:
        p.map(partial_running, tuple_list)

parser = argparse.ArgumentParser(description='')
parser.add_argument('--model', '-m', help='one of mix123 mix12 aa aa_c20 part123',
                    required=True)
parser.add_argument('--start', '-r1', help='', 
                    required=True)
parser.add_argument('--end', '-r2', help='', 
                    required=True)
parser.add_argument('--n_pool', '-p', help='', 
                    required=True)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        control(args.model, args.start, args.end, args.n_pool)
    except Exception as e:
        print(e)

