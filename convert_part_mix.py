filename = 'partition.iqtree'


len_list = []
q_para_list = []

with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if '	DNA	' in line:
            len_list.append(float(line.split()[3]))
        if '  GTR{' in line:
            model_para_list = line.split()[3].split('+')
            q_para = model_para_list[0] + '+' + model_para_list[1]
            q_para_list.append(q_para)

assert len(len_list) == len(q_para_list)
            
weight_list = [n/sum(len_list) for n in len_list]            
            
cmd_str = "MIX\"{"            
for i in range(len(weight_list)):
    if i == 0:
        cmd_str = cmd_str + q_para_list[i] + ":1:" + str(weight_list[i])
    else:
        cmd_str = cmd_str + "," + q_para_list[i] + ":1:" + str(weight_list[i])
cmd_str = cmd_str + "}\"+I+G"            
            
with open(filename + '.param', 'w+') as f:
    f.write(cmd_str)            
            
            
            
            
            