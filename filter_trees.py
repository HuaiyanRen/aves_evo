from ete3 import Tree

with open("14972_exon_alns_namelist.txt") as f:
    f_list = f.readlines()
    
output_file = 'filtered_trees.txt'
with open(output_file, 'w+') as f:
    a =1

for i in range(200):
    f_name = f_list[i].split(" ")[1]
    tree_file = 'trees/' + f_name.split(".")[0] +".treefile"

    treestr = open(tree_file,'r').read()
    tree = Tree(treestr,format = 1)
    
    with open(output_file, 'a+') as f:
        f.write(tree.write(format = 9) + '\n')


