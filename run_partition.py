from multiprocessing import Pool
from functools import partial
import subprocess
import numpy as np


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

def running_i(i):

    
    f_name = f_list[i].split(" ")[1]
    out_name = '14972_exon_results/'+str(i) + '_' +f_name.split(".")[0]

    cmd1 = '/usr/bin/time -v /data/huaiyan/software/iqtree-2.3.5.onnxupdate-Linux-intel/bin/iqtree2 -m MIX+MFP -mset GTR -mrate E,I,G,I+G,R,I+R -pre '+out_name+ ' -nt 1 -s 14972_exon_alns/'+f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'w') as f:
        #f.write(result.stdout)
        f.write(result.stderr)

# 14972
i_list = list(np.arange(0, 200, 1))


partial_running = partial(running_i)

with Pool(40) as p:
    score_list = p.map(partial_running, i_list)

