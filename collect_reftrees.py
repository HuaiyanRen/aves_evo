

iqtree_folder = 'gene_trees/'
output_file = 'astral_trees/ref_chr1.txt'


with open("chr1_namelist_random.txt") as f:
    f_list = f.readlines()


name_list = []
treefile_list = []
n =0
for i in range(0,1266):
    #if i not in [3, 9, 11, 24, 27, 28, 29, 44, 50, 65, 76, 80, 95, 96]:
        loci_name = f_list[i].split(" ")[1].split('.')[0]
        #tree_name = iqtree_folder  + loci_name +'.treefile'
        
        #treefile_list.append(tree_name)
        name_list.append(loci_name)
        #n = n + 1

with open('63430.named.gene.trees') as f:
    for line in f.readlines():
        if line.split('_1k')[0] in name_list:
            treefile_list.append(line.split()[1])            
            n = n + 1

print(n)
print(name_list)

with open(output_file, 'w') as output_file:
    for treefile in treefile_list:
        output_file.write(treefile)