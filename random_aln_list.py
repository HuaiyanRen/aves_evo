import os

file_names = os.listdir("chr1")
file_names = sorted(file_names)

import random
random.seed(20240930)
aln_list = list(range(len(file_names)))
random.shuffle(aln_list)

with open("chr1_namelist_random.txt", 'w') as f:
    for i in range(len(file_names)):
        file_name = file_names[aln_list[i]]        
        f.write(f"{i} {file_name}\n") 
        
        
