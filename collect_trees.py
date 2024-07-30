import os

folder_name = '14972_exon_results'

folder_path = os.getcwd()
tree_path = os.path.join(folder_path,folder_name)
output_file = folder_name + '_trees.txt'

treefile_list = []
n = 0
for file in os.listdir(tree_path):
    if file.endswith('.treefile'):
        #file_order = int(file.split('_')[0])
        #if file_order in list1:
        treefile_list.append(file)
        n = n + 1
        #print(file)
print(n)

with open(output_file, 'w') as output_file:
    for treefile in treefile_list:
        treefile_path = os.path.join(tree_path, treefile)
        with open(treefile_path, 'r') as current_file:
            output_file.write(current_file.read())