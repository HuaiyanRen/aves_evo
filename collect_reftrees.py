

iqtree_folder = 'gene_trees/'
output_file = 'astral_trees/ref_2k.txt'


with open("exon_namelist_random.txt") as f:
    f_list = f.readlines()



treefile_list = []
n =0
for i in range(0,2000):
    #if i not in [3, 9, 11, 24, 27, 28, 29, 44, 50, 65, 76, 80, 95, 96]:
        loci_name = f_list[i].split(" ")[1].rstrip()
        tree_name = iqtree_folder  + loci_name +'.treefile'
        
        treefile_list.append(tree_name)
        n = n + 1

print(n)

with open(output_file, 'w') as output_file:
    for treefile in treefile_list:
        with open(treefile, 'r') as current_file:
            output_file.write(current_file.read())