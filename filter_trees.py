from ete3 import Tree

input_file = r'C:\Users\u7151703\OneDrive - Australian National University\Desktop\research\aves_datasets\named.trees'
output_file =  r'C:\Users\u7151703\OneDrive - Australian National University\Desktop\research\aves_datasets\exon14k_trees.txt'

treefile_list = []
with open(input_file) as f:
    for line in f.readlines():
        treefile_list.append(line.split()[1].replace("/", ""))


with open(output_file, 'w') as output_file:
    for treefile in treefile_list:
        output_file.write(treefile +'\n')
        
        
