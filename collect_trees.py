import os
import csv 

iqtree_folder = 'aa/'
output_file = 'astral_trees/aa.txt'
result_csv = 'astral_trees/aa.csv'
with open(result_csv,'w+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    csv_write.writerow(['name', 'tree_exist'])


with open("14972_exon_alns_namelist.txt") as f:
    f_list = f.readlines()



treefile_list = []
n =0
for i in range(0,100):
    loci_name = f_list[i].split(" ")[1].split('.')[0]
    tree_name = iqtree_folder + str(i) + '_' + f_list[i].split(" ")[1].split('.')[0] +'.treefile'
        
    if os.path.isfile(tree_name):
        #file_order = int(file.split('_')[0])
        #if file_order in list1:
        treefile_list.append(tree_name)
        n = n + 1
        tree_exist = True
    else:
        print(loci_name)
        tree_exist = False
        
    result_row = [loci_name, tree_exist]

    with open(result_csv,'a+',newline='') as csvf:
        csv_write = csv.writer(csvf)
        csv_write.writerow(result_row)  
           
print(n)

with open(output_file, 'w') as output_file:
    for treefile in treefile_list:
        with open(treefile, 'r') as current_file:
            output_file.write(current_file.read())
            