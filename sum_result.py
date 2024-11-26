import os
import csv

with open('result_total.csv','w+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    csv_write.writerow(['name', 'num',
                        'classes', 'ntaxa', 'nsites', 'pythia_score',
                        'rf', 'nrf'])

with open("exon_namelist_random.txt") as f:
    f_list = f.readlines()

for i in range(0,2000):   
    
    name = f_list[i].split(" ")[1].rstrip() 
    
    with open('mix_c12/'+str(i) + '_' + name + '.iqtree') as iq_f:
        for line in iq_f.readlines():
            if 'Input data: ' in line:
                ntaxa = float(line.split()[-6])
                nsites = float(line.split()[-3])
            if 'odel of substitution:' in line:
                classes =line.count(',') + 1

    if os.path.isfile('sin_c12/'+str(i) + '_' + name + '.uniqueseq.phy'):
        with open('sin_c12/'+str(i) + '_' + name + '.uniqueseq.phy') as iq_f:
            line = iq_f.readlines()[0]
            line = line.strip()
            ntaxa = float(line.split()[0])    

    pythia_score = 0    
    with open('rf_compare/'+str(i) + '_' + name + '_pythia.txt') as b:
        for line in b.readlines():
            if 'The predicted difficulty for MSA' in line:
                pythia_score = float(line.split()[-1])

    if 2*ntaxa-6 > 0:         
        with open('rf_compare/'+str(i) + '_' + name + '_rf.rfdist') as b:
            for line in b.readlines():
                if 'Tree0' in line:
                    rf = float(line.split()[-1])
                    nrf = rf/(2*ntaxa-6)
                    
        result_row = [name, i, classes, ntaxa, nsites, pythia_score, rf, nrf]
    else:
        result_row = [name, i, classes, ntaxa, nsites, pythia_score, 0, 0]
    
    with open('result_total.csv','a+',newline='') as csvf:
        csv_write = csv.writer(csvf)
        csv_write.writerow(result_row) 

        