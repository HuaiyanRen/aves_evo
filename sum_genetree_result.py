import os
import csv

with open("exon_namelist_random.txt") as f:
    f_list = f.readlines()

folder = 'sin_c12'
result_csv = 'rf_' +  folder + '.csv'
with open(result_csv,'w+',newline='') as csvf:
    csv_write = csv.writer(csvf)
    csv_write.writerow(['name', 'model', 
                        'rf_main', 'rf_exon', 'rf_gene',
                        'nrf_main', 'nrf_exon', 'nrf_gene'])

for i in range(0,2000):
    name = f_list[i].split(" ")[1].rstrip()
    
    if not os.path.isfile(folder + '/'+str(i) + '_' + name + '.uniqueseq.phy'):
        with open(folder + '/'+str(i) + '_' + name + '.iqtree') as iq_f:
            for line in iq_f.readlines():
                if 'Input data: ' in line:
                    ntaxa = float(line.split()[-6])       
    else:
        with open(folder + '/'+str(i) + '_' + name + '.uniqueseq.phy') as iq_f:
            line = iq_f.readlines()[0]
            line = line.strip()
            ntaxa = float(line.split()[0])
        
    if 2*ntaxa-6  > 0:         
        with open(folder + '/'+str(i) + '_' + name + '_rfmain.rfdist') as b:
            for line in b.readlines():
                if 'Tree0' in line:
                    rfmain = float(line.split()[-1])
                    nrfmain = rfmain/(2*ntaxa-6)
                    
        with open(folder + '/'+str(i) + '_' + name + '_rfexon.rfdist') as b:
            for line in b.readlines():
                if 'Tree0' in line:
                    rfexon = float(line.split()[-1])
                    nrfexon = rfexon/(2*ntaxa-6)
        
        with open(folder + '/'+str(i) + '_' + name + '_rfgene.rfdist') as b:
            for line in b.readlines():
                if 'Tree0' in line:
                    rfgene = float(line.split()[-1])
                    nrfgene = rfgene/(2*ntaxa-6)
        
        result_row = [name, folder,
                      rfmain, rfexon, rfgene,
                      nrfmain, nrfexon, nrfgene]
    else:
        result_row = [name, folder,
                      0, 0, 0,
                      0, 0, 0]
    
    with open(result_csv,'a+',newline='') as csvf:
        csv_write = csv.writer(csvf)
        csv_write.writerow(result_row) 

