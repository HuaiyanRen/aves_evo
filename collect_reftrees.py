iqtree_folder = 'gene_trees/'
output_file = 'astral_trees/refgene100.txt'


with open("14972_exon_alns_namelist.txt") as f:
    f_list = f.readlines()



treefile_list = []
n =0
for i in range(0,100):
    loci_name = f_list[i].split(" ")[1].split('.')[0]
    tree_name = iqtree_folder  + f_list[i].split(" ")[1].split('.')[0] +'.treefile'
        
    treefile_list.append(tree_name)
    n = n + 1

print(n)

with open(output_file, 'w') as output_file:
    for treefile in treefile_list:
        with open(treefile, 'r') as current_file:
            output_file.write(current_file.read())