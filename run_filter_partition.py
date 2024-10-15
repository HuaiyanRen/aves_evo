from multiprocessing import Pool
from functools import partial
import subprocess
import numpy as np
import argparse
import sys
import os

# =============================================================================
# import pandas as pd
# taxa_file = r"C:\Users\u7151703\OneDrive - Australian National University\Desktop\research\aves_evo\draft_results\taxa_filter.csv"
# 
# df = pd.read_csv(taxa_file)
# filtered_df = df[df['filter_to_2'] != True]
# result_string = ' '.join(filtered_df['label'].astype(str))
# print(result_string)
# =============================================================================

# =============================================================================
# file_names = os.listdir("c12")
# file_names = sorted(file_names)
# 
# import random
# random.seed(20240905)
# exon_list = list(range(len(file_names)))
# random.shuffle(exon_list)
# 
# with open("exon_namelist_random.txt", 'w') as f:
#     for i in range(len(file_names)):
#         file_name = file_names[exon_list[i]].split('.')[0]        
#         f.write(f"{i} {file_name}\n") 
# =============================================================================

# filter 3
# result_string = 'COLVIR ODOGUJ COTJAP PHACOL TYMCUP NUMMEL PENPIL ALELAT ANSSEM CAIMOS ANAPLA ANAZON ACACHL CNELOR MELVER PROCAF DICEXI LEPASP CHLCYA CHLHAR IRECYA PEUTAE PRUFUL PRUHIM PASDOM HYPCIN MOTALB CHLVIR HEMWIL SERCAN LOXCUR LOXLEU RHOROS CALORN EMBFUC PHEMEL CARCAR PASAMO NESACU GEOFOR SPOHYP SPIPAS MELMEL JUNHYE ZONALB SETCOR SETKIR AGEPHO MOLATE QUIMEX UROPYL PLONIG VIDCHA VIDMAC LONSTR TAEGUT BOMGAR PHANIT REGSAT TICMUR SITEUR POLCAE THRLUD CERBRA CERFAM ELAFOR BUPERY TOXRED RHAINO LEUROT STUVUL CINMEX CATFUS CERCOR COPSEC ERIRUB FICALB OENOEN SAXMAU ANTMIN POEATR PARMAJ PSEHUM ALACHE PANBIA NICCHL SYLVIR CISJUN ACRARU HIPICT LOCOCH OXYMAD DONATR HIRRUS PHYTRO RHASIB HYLPRA AEGCAU ERYMCC CETCET HORVUL BRAATR PYCJOC SINWEB SYLATR SYLBOR STEDEN ZOSHYP ZOSLAT PORRUF ILLCLE LEILUT DRYBRU CHAFRE PICGYM CALWIL NOTCIN PTILEU EDOCOE CHAPAP RHIDAH DICMEG MYIHEB STRCIN IFRKOW PARRAG LANLUD APHCOE CORMON CORBRA CORCOR MOHOCH MACNIG GYMTIB RHALEU DRYGAM DYACAS MYSCRO DAPCHR EULNIG ALERUF FALFRO PACPHI ORIORI OREARF PTEMEL ERPZAN VIRALT ORTSPA POSRUF MALELE DASBRO GRAPIC ORISOL PARPUN CLIRUF PTIVIO ATRCLA MENNOV NEOCOR SERLUN SAPAEN PITSOR CALVIR SMICAP RHEHOF SAKLUC GRAVAR SCYSUP FORRUF SCLMEX FURFIG CAMPRO XIPELE LEPCOR MANMAN CEPORN PACMIN ONYCOR OXYCRI PIPCHL NEOCIN TACRUB MIOMAC TYRSAV EOLROS AMAGUI AGAROS BUCABY BRALEP EURGUL TODMEX BARMAR CHLAEN BUCCAP GALDEA PICPUB PSIHAE RAMSUL SEMFRA CICNIG CATAUR CIRPEC HALLEU AQUCHR SPITYR THACHL FREGRA HYDTET FULGLA CICMAG MESCAY COCCOC EGRGAR BALREX SCOUMB SULDAC ANHANH ANHRUF PHACAR URIPEL NANHAR NANAUR NANBRA NYCLEU ANTCAR CHOACU NYCBRA NYCGRA PODSTR AEGBEN CHAPEL HEMCOM BURBIS CHIMIN PLUSOC CHAALE HIMHIM LIMLAP AREINT CALPUG PEDTOR THIORB JACJAC NYCSEM ROSBEN TURVEL DROARD GLAPRA RHIAFR STEPAR CEPGRY URIAAL URILOM PHASIM RYNNIG RISTRI CHRMAC LARSMI HELFUL PSOCRE ARAGUA BALREG SYRPAR COLPIC COLLIV CENUNI CUCCAN CEUAER PIACAY APTROW EUDELE NOTPER NOTJUL NOTNIG CRYSOU CRYCIN CRYUND'

# filter 2
result_string = 'CALSQU COLVIR ODOGUJ GALGAL COTJAP PHACOL MELGAL NUMMEL PENPIL ANSSEM ANSCYG CAIMOS ASASCU ANAPLA MELVER PROCAF DICEXI CHLCYA CHLHAR IRECYA PEUTAE PRUFUL PRUHIM PASDOM HYPCIN MOTALB CHLVIR HEMWIL SERCAN LOXCUR LOXLEU RHOROS CALORN EMBFUC PHEMEL CARCAR PASAMO NESACU GEOFOR SPOHYP SPIPAS MELMEL JUNHYE ZONALB SETCOR SETKIR AGEPHO MOLATE UROPYL PLONIG VIDCHA VIDMAC LONSTR TAEGUT PHANIT REGSAT SITEUR POLCAE THRLUD CERBRA ELAFOR BUPERY TOXRED RHAINO LEUROT CINMEX CATFUS CERCOR COPSEC ERIRUB FICALB SAXMAU ANTMIN POEATR PARMAJ ALACHE PANBIA NICCHL SYLVIR CISJUN ACRARU HIPICT LOCOCH OXYMAD DONATR HIRRUS PHYTRO RHASIB HYLPRA AEGCAU ERYMCC CETCET HORVUL BRAATR PYCJOC SINWEB SYLATR SYLBOR STEDEN ZOSHYP PORRUF ILLCLE LEILUT DRYBRU CHAFRE PICGYM CALWIL NOTCIN PTILEU EDOCOE CHAPAP RHIDAH DICMEG MYIHEB STRCIN IFRKOW PARRAG LANLUD APHCOE CORMON CORBRA MOHOCH MACNIG GYMTIB RHALEU DRYGAM DYACAS MYSCRO DAPCHR EULNIG ALERUF FALFRO PACPHI ORIORI OREARF PTEMEL ERPZAN ORTSPA POSRUF MALELE DASBRO GRAPIC ORISOL PARPUN CLIRUF PTIVIO MENNOV SERLUN SAPAEN PITSOR CALVIR RHEHOF GRAVAR SCYSUP FORRUF SCLMEX FURFIG CAMPRO LEPCOR CEPORN PACMIN ONYCOR OXYCRI PIPCHL NEOCIN TACRUB MIOMAC NESNOT EOLROS AMAGUI AGAROS FALPER BUCABY RHICYA MERNUB EURGUL TODMEX BARMAR CEYCYA CHLAEN GALDEA PICPUB INDMAC PSIHAE TRILEU EUBBOU RAMSUL GLABRA CICNIG SAGSER PANHAL CIRPEC HALLEU AQUCHR SPITYR THACHL FREGRA HYDTET FULGLA PELURI CICMAG MESCAY NIPNIP COCCOC EGRGAR BALREX SCOUMB FREMAG SULDAC ANHANH ANHRUF PHACAR URIPEL NANHAR NANAUR NYCLEU ANTCAR STECAR NYCBRA NYCGRA PODSTR AEGBEN CHAPEL HEMCOM CALANN BURBIS CHIMIN CHAALE CHAVOC HIMHIM IBISTR LIMLAP AREINT CALPUG PEDTOR THIORB JACJAC NYCSEM ROSBEN TURVEL DROARD GLAPRA RHIAFR STEPAR CEPGRY ALCTOR URIAAL PHASIM RYNNIG RISTRI CHRMAC LARSMI HELFUL ZAPATR PSOCRE ARAGUA BALREG SYRPAR CALNIC COLPIC COLLIV CORCRI ARDKOR CROSUL CENBEN CENUNI CUCCAN PIACAY APTOWE APTROW EUDELE NOTPER NOTORN NOTJUL NOTNIG TINGUT CRYSOU CRYCIN'

with open("exon_namelist_random.txt") as f:
    f_list = f.readlines()

def run_mix123(tuple_list):   
    model, i = tuple_list
    
    if not os.path.exists('c123_filtered3'):
        os.makedirs('c123_filtered3')
    if not os.path.exists('mix_c123_filtered3'):
        os.makedirs('mix_c123_filtered3')
        
    name = f_list[i].split(" ")[1].rstrip()    
    f_name = 'c123/'+ name + '.cds.fa'
    filtered_f_name = 'c123_filtered3/'+ name + '.cds.fa-out.fas'
    if not os.path.isfile(filtered_f_name):
        filter_cmd = 'python3 AMAS.py remove -x ' + result_string + ' -d dna -f fasta -i ' + f_name + ' -u fasta -g c123_filtered3/'
        os.system(filter_cmd)
    
    out_name = 'mix_c123_filtered3/'+str(i) + '_' + name

    cmd1 = '/usr/bin/time -v /home/remote/u7151703/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m MIX+MFP -mset GTR -mrate E,I,G,I+G -wspm -pre '+out_name+ ' -nt 1 -s ' + filtered_f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'a+') as f:
        #f.write(result.stdout)
        f.write(result.stderr)

def run_mix12(tuple_list):      
    model, i = tuple_list 
    
    if not os.path.exists('c12_filtered3'):
        os.makedirs('c12_filtered3')
    if not os.path.exists('mix_c12_filtered3'):
        os.makedirs('mix_c12_filtered3')
    
    name = f_list[i].split(" ")[1].rstrip() 
    f_name = 'c12/'+ name + '.cds.fa'
    filtered_f_name = 'c12_filtered3/'+ name + '.cds.fa-out.fas'
    if not os.path.isfile(filtered_f_name):
        filter_cmd = 'python3 AMAS.py remove -x ' + result_string + ' -d dna -f fasta -i ' + f_name + ' -u fasta -g c12_filtered3/'
        os.system(filter_cmd)
    
    out_name = 'mix_c12_filtered3/'+str(i) + '_' + name

    cmd1 = '/usr/bin/time -v /home/remote/u7151703/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m MIX+MFP -mset GTR -mrate E,I,G,I+G -wspm -pre '+out_name+ ' -nt 1 -s ' + filtered_f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'a+') as f:
        #f.write(result.stdout)
        f.write(result.stderr)
 
def run_c1123(tuple_list):   
    model, i = tuple_list
    
    if not os.path.exists('c123_filtered3'):
        os.makedirs('c123_filtered3')
    if not os.path.exists('c1_c123_filtered3'):
        os.makedirs('c1_c123_filtered3')
        
    name = f_list[i].split(" ")[1].rstrip()    
    f_name = 'c123/'+ name + '.cds.fa'
    filtered_f_name = 'c123_filtered3/'+ name + '.cds.fa-out.fas'
    if not os.path.isfile(filtered_f_name):
        filter_cmd = 'python3 AMAS.py remove -x ' + result_string + ' -d dna -f fasta -i ' + f_name + ' -u fasta -g c123_filtered3/'
        os.system(filter_cmd)
    
    out_name = 'c1_c123_filtered3/'+str(i) + '_' + name

    cmd1 = '/usr/bin/time -v /home/remote/u7151703/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m MFP -mset GTR -mfreq FO -mrate E,I,G,I+G -pre '+out_name+ ' -nt 1 -s ' + filtered_f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'a+') as f:
        #f.write(result.stdout)
        f.write(result.stderr)

def run_c112(tuple_list):   
    model, i = tuple_list
    
    if not os.path.exists('c12_filtered3'):
        os.makedirs('c12_filtered3')
    if not os.path.exists('c1_c12_filtered3'):
        os.makedirs('c1_c12_filtered3')
        
    name = f_list[i].split(" ")[1].rstrip()    
    f_name = 'c12/'+ name + '.cds.fa'
    filtered_f_name = 'c12_filtered3/'+ name + '.cds.fa-out.fas'
    if not os.path.isfile(filtered_f_name):
        filter_cmd = 'python3 AMAS.py remove -x ' + result_string + ' -d dna -f fasta -i ' + f_name + ' -u fasta -g c12_filtered3/'
        os.system(filter_cmd)
    
    out_name = 'c1_c12_filtered3/'+str(i) + '_' + name

    cmd1 = '/usr/bin/time -v /home/remote/u7151703/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m MFP -mset GTR -mfreq FO -mrate E,I,G,I+G -pre '+out_name+ ' -nt 1 -s ' + filtered_f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'a+') as f:
        #f.write(result.stdout)
        f.write(result.stderr)        
 
def run_part123(tuple_list):   
    model, i = tuple_list
    
    if not os.path.exists('c123_filtered3'):
        os.makedirs('c123_filtered3')
    if not os.path.exists('part_c123_filtered3'):
        os.makedirs('part_c123_filtered3')
    
    name = f_list[i].split(" ")[1].rstrip() 
    f_name = 'c123/'+ name + '.cds.fa'
    filtered_f_name = 'c123_filtered3/'+ name + '.cds.fa-out.fas'
    if not os.path.isfile(filtered_f_name):
        filter_cmd = 'python3 AMAS.py remove -x ' + result_string + ' -d dna -f fasta -i ' + f_name + ' -u fasta -g c123_filtered3/'
        os.system(filter_cmd)    

    part_name = 'c123_filtered3/'+ name + '_part.nex'
    if not os.path.isfile(part_name):
        amas_cmd = 'python3 AMAS.py concat -f fasta -d dna -i ' + filtered_f_name + ' -u fasta -p ' + part_name + ' -n 123 --part-format nexus -t ' + filtered_f_name
        os.system(amas_cmd)

    out_name = 'part_c123_filtered3/'+str(i) + '_' + name

    cmd1 = '/usr/bin/time -v /home/remote/u7151703/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m TESTMERGE -mset GTR -mfreq FO -pre '+out_name+ ' -nt 1 -s '+ filtered_f_name + ' -p '+part_name
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'a+') as f:
        #f.write(result.stdout)
        f.write(result.stderr)

def run_part12(tuple_list):   
    model, i = tuple_list
    
    if not os.path.exists('c12_filtered3'):
        os.makedirs('c12_filtered3')
    if not os.path.exists('part_c12_filtered3'):
        os.makedirs('part_c12_filtered3')
    
    name = f_list[i].split(" ")[1].rstrip() 
    f_name = 'c12/'+ name + '.cds.fa'
    filtered_f_name = 'c12_filtered3/'+ name + '.cds.fa-out.fas'
    if not os.path.isfile(filtered_f_name):
        filter_cmd = 'python3 AMAS.py remove -x ' + result_string + ' -d dna -f fasta -i ' + f_name + ' -u fasta -g c12_filtered3/'
        os.system(filter_cmd)    

    part_name = 'c12_filtered3/'+ name + '_part.nex'
    if not os.path.isfile(part_name):
        amas_cmd = 'python3 AMAS.py concat -f fasta -d dna -i ' + filtered_f_name + ' -u fasta -p ' + part_name + ' -n 12 --part-format nexus -t ' + filtered_f_name
        os.system(amas_cmd)

    out_name = 'part_c12_filtered3/'+str(i) + '_' + name

    cmd1 = '/usr/bin/time -v /home/remote/u7151703/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m TESTMERGE -mset GTR -mfreq FO -pre '+out_name+ ' -nt 1 -s '+ filtered_f_name + ' -p '+part_name
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'a+') as f:
        #f.write(result.stdout)
        f.write(result.stderr)

def run_aa(tuple_list):     
    model, i = tuple_list
    
    if not os.path.exists('pep_filtered3'):
        os.makedirs('pep_filtered3')
    if not os.path.exists('aa_filtered3'):
        os.makedirs('aa_filtered3')
    
    name = f_list[i].split(" ")[1].rstrip() 
    f_name = 'pep/'+ name + '.pep.fa'
    filtered_f_name = 'aa_filtered3/'+ name + '.pep.fa-out.fas'
    if not os.path.isfile(filtered_f_name):
        filter_cmd = 'python3 AMAS.py remove -x ' + result_string + ' -d aa -f fasta -i ' + f_name + ' -u fasta -g pep_filtered3/'
        os.system(filter_cmd)
        
    out_name = 'aa_filtered3/'+str(i) + '_' + name

    cmd1 = '/usr/bin/time -v /home/remote/u7151703/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m MFP -mrate E,I,G,I+G -pre '+ out_name + ' -nt 1 -s '+ filtered_f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'a+') as f:
        #f.write(result.stdout)
        f.write(result.stderr)
        
def run_aa_c20(tuple_list):     
    model, i = tuple_list  
    
    if not os.path.exists('pep_filtered3'):
        os.makedirs('pep_filtered3')
    if not os.path.exists('aa_filtered3'):
        os.makedirs('aa_c20_filtered3')
    
    name = f_list[i].split(" ")[1].rstrip() 
    f_name = 'pep/'+ name + '.pep.fa'
    filtered_f_name = 'aa_filtered3/'+ name + '.pep.fa-out.fas'
    if not os.path.isfile(filtered_f_name):
        filter_cmd = 'python3 AMAS.py remove -x ' + result_string + ' -d aa -f fasta -i ' + f_name + ' -u fasta -g pep_filtered3/'
        os.system(filter_cmd)
        
    out_name = 'aa_c20_filtered3/'+str(i) + '_' + name
        
    cmd1 = '/usr/bin/time -v /home/remote/u7151703/software/iqtree-2.3.5.1.mixfinder-Linux-intel/bin/iqtree2 -m Q.bird+C20+I+G -pre '+ out_name + ' -nt 1 -s '+ filtered_f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'a+') as f:
        #f.write(result.stdout)
        f.write(result.stderr)

# 14972
def control(model, start, end, n_pool):
    if model not in ['mix123', 'mix12', 'c1123', 'c112', 'aa', 'aa_c20', 'part123', 'part12']:
        print("wrong model type")
        sys.exit(1)
           
    start = int(start)
    end = int(end)
    n_pool = int(n_pool)
# =============================================================================
#     if model == 'aa_c20':
#         n_pool = int(n_pool/3)
# =============================================================================
    
    replicates = list(np.arange(start,end,1))
    
    tuple_list = ['']*len(replicates)

    for i in range(len(tuple_list)):
        tuple_list[i] = model, replicates[i]
        
    if model == 'mix123':
        partial_running = partial(run_mix123)
    elif model == 'c1123':
        partial_running = partial(run_c1123)
    elif model == 'c112':
        partial_running = partial(run_c112)
    elif model == 'mix12':
        partial_running = partial(run_mix12)
    elif model == 'part123':
        partial_running = partial(run_part123)
    elif model == 'part12':
        partial_running = partial(run_part12)
    elif model == 'aa':
        partial_running = partial(run_aa)
    elif model == 'aa_c20':
        partial_running = partial(run_aa_c20)   
        
    with Pool(n_pool) as p:
        p.map(partial_running, tuple_list)

parser = argparse.ArgumentParser(description='')
parser.add_argument('--model', '-m', help='one of mix123 mix12 aa aa_c20 part123',
                    required=True)
parser.add_argument('--start', '-r1', help='', 
                    required=True)
parser.add_argument('--end', '-r2', help='', 
                    required=True)
parser.add_argument('--n_pool', '-p', help='', 
                    required=True)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        control(args.model, args.start, args.end, args.n_pool)
    except Exception as e:
        print(e)
