tree_folder = 'exon_trees/'
output_file = 'astral_trees/ref_f90p.txt'


with open("exon_namelist_random.txt") as f:
    f_list = f.readlines()


name_list = []
treefile_list = []
n =0
for i in range(0,14792):

    loci_name = f_list[i].split(" ")[1].rstrip()
    
    
    pythia_score = 1    
    with open('rf_compare/'+str(i) + '_' + loci_name + '_pythia.txt') as b:
        for line in b.readlines():
            if 'The predicted difficulty for MSA' in line:
                pythia_score = float(line.split()[-1])
                
    if pythia_score < 0.9:
        tree_name = tree_folder  + loci_name +'.treefile'
        treefile_list.append(tree_name)
        n = n + 1

    

print(n)

with open(output_file, 'w') as output_file:
    for treefile in treefile_list:
        with open(treefile, 'r') as current_file:
            output_file.write(current_file.read())