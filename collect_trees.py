import os
import csv 

iqtree_folder = 'mix_c12/'
output_file = 'astral_trees/mix12_2k_f2c.txt'
# =============================================================================
# result_csv = 'astral_trees/aa.csv'
# with open(result_csv,'w+',newline='') as csvf:
#     csv_write = csv.writer(csvf)
#     csv_write.writerow(['name', 'tree_exist'])
# =============================================================================


with open("exon_namelist_random.txt") as f:
    f_list = f.readlines()

treefile_list = []
exclude_list = []
n =0
for i in []:
        loci_name = f_list[i].split(" ")[1].rstrip() 
        iqtree_name = iqtree_folder + str(i) + '_' + loci_name +'.iqtree'
        tree_name = iqtree_folder + str(i) + '_' + loci_name +'.treefile'
         
        if os.path.isfile(iqtree_name):
            #file_order = int(file.split('_')[0])
            #if file_order in list1:
            treefile_list.append(tree_name)
            n = n + 1
            tree_exist = True
        else:
            print(loci_name)
            exclude_list.append(i)
            tree_exist = False
            
# =============================================================================
#         result_row = [loci_name, tree_exist]
#     
#         with open(result_csv,'a+',newline='') as csvf:
#             csv_write = csv.writer(csvf)
#             csv_write.writerow(result_row)  
# =============================================================================
           
print(n)
print(exclude_list)

with open(output_file, 'w') as output_file:
    for treefile in treefile_list:
        with open(treefile, 'r') as current_file:
            output_file.write(current_file.read())
            