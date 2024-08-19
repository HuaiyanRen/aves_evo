import pandas as pd

probfile = "mixture.siteprob"
iqtreefile = "mixture.iqtree"
mix_to_part = "mix_to_part.param.nex"

df = pd.read_csv(probfile, sep='\t')
df = df.drop('Site', axis=1)
column_names = list(df.columns)

part_dict = {}
for column in column_names:
    key_name = 'q' + column[1:]
    part_dict[key_name] = []

for i in range(0, len(df)):
    class_idx = 'q' + df.idxmax(axis=1)[i][1:] 
    part_dict[class_idx].append(i+1)

lines = ['#NEXUS', 'Begin sets;']

for i in range(len(part_dict)):
    key_str = 'q' + str(i+1)
    part_str = '\tcharset ' + key_str + ' = ' + ' '.join(map(str, part_dict[key_str])) + ';'
    lines.append(part_str)
    
lines.append('\tcharpartition mymodels =')

param_list = []
with open(iqtreefile, 'r') as file:
    f_lines = file.readlines()
    for line in f_lines:
        if '  GTR           1.0000' in line:
            param_str = '\t\t' + line.split()[-1] + '+I+G: q'
            param_list.append(param_str)
        
for i in range(len(param_list)):
    if i == len(param_list)-1:
        lines.append(param_list[i] + str(i+1) + ';')
    else:
        lines.append(param_list[i] + str(i+1) + ',')        
lines.append('End;')

        
with open(mix_to_part, 'a+') as f:
    for line in lines:
        f.write(line + '\n')

