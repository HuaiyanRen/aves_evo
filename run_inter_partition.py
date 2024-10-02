from multiprocessing import Pool
from functools import partial
import subprocess
import numpy as np
import argparse
import sys
import os



# filter 3
result_string = 'Colinus_virginianus Odontophorus_gujanensis Coturnix_japonica Phasianus_colchicus Tympanuchus_cupido Numida_meleagris Penelope_pileata Alectura_lathami Anseranas_semipalmata Cairina_moschata Anas_platyrhynchos Anas_zonorhyncha Acanthisitta_chloris Cnemophilus_loriae Melanocharis_versteri Promerops_cafer Dicaeum_eximium Leptocoma_aspasia Chloropsis_cyanopogon Chloropsis_hardwickii Irena_cyanogastra Peucedramus_taeniatus Prunella_fulvescens Prunella_himalayana Passer_domesticus Hypocryptadius_cinnamomeus Motacilla_alba Chlorodrepanis_virens Hemignathus_wilsoni Serinus_canaria Loxia_curvirostra Loxia_leucoptera Rhodinocichla_rosea Calcarius_ornatus Emberiza_fucata Pheucticus_melanocephalus Cardinalis_cardinalis Passerina_amoena Nesospiza_acunhae Geospiza_fortis Sporophila_hypoxantha Spizella_passerina Melospiza_melodia Junco_hyemalis Zonotrichia_albicollis Setophaga_coronata Setophaga_kirtlandii Agelaius_phoeniceus Molothrus_ater Quiscalus_mexicanus Urocynchramus_pylzowi Ploceus_nigricollis Vidua_chalybeata Vidua_macroura Lonchura_striata Taeniopygia_guttata Bombycilla_garrulus Phainopepla_nitens Regulus_satrapa Tichodroma_muraria Sitta_europaea Polioptila_caerulea Thryothorus_ludovicianus Certhia_brachydactyla Certhia_familiaris Elachura_formosa Buphagus_erythrorhynchus Toxostoma_redivivum Rhabdornis_inornatus Leucopsar_rothschildi Sturnus_vulgaris Cinclus_mexicanus Catharus_fuscescens Cercotrichas_coryphaeus Copsychus_sechellarum Erithacus_rubecula Ficedula_albicollis Oenanthe_oenanthe Saxicola_maurus Anthoscopus_minutus Poecile_atricapillus Parus_major Pseudopodoces_humilis Alaudala_cheleensis Panurus_biarmicus Nicator_chloris Sylvietta_virens Cisticola_juncidis Acrocephalus_arundinaceus Hippolais_icterina Locustella_ochotensis Oxylabes_madagascariensis Donacobius_atricapilla Hirundo_rustica Phylloscopus_trochilus Rhadina_sibilatrix Hylia_prasina Aegithalos_caudatus Erythrocercus_mccallii Cettia_cetti Horornis_vulcanius Brachypodius_atriceps Pycnonotus_jocosus Sinosuthora_webbiana Sylvia_atricapilla Sylvia_borin Sterrhoptilus_dennistouni Zosterops_hypoxanthus Zosterops_lateralis Pomatorhinus_ruficollis Illadopsis_cleaveri Leiothrix_lutea Drymodes_brunneopygia Chaetops_frenatus Picathartes_gymnocephalus Callaeas_wilsoni Notiomystis_cincta Ptilorrhoa_leucosticta Edolisoma_coerulescens Chaetorhynchus_papuensis Rhipidura_dahli Dicrurus_megarhynchus Myiagra_hebetior Struthidea_cinerea Ifrita_kowaldi Paradisaea_raggiana Lanius_ludovicianus Aphelocoma_coerulescens Corvus_moneduloides Corvus_brachyrhynchos Corvus_cornix Mohoua_ochrocephala Machaerirhynchus_nigripectus Gymnorhina_tibicen Rhagologus_leucostigma Dryoscopus_gambensis Dyaphorophyia_castanea Mystacornis_crossleyi Daphoenositta_chrysoptera Eulacestoma_nigropectus Aleadryas_rufinucha Falcunculus_frontatus Pachycephala_philippinensis Oriolus_oriolus Oreocharis_arfaki Pteruthius_melanotis Erpornis_zantholeuca Vireo_altiloquus Orthonyx_spaldingii Pomatostomus_ruficeps Malurus_elegans Dasyornis_broadbenti Grantiella_picta Origma_solitaria Pardalotus_punctatus Climacteris_rufus Ptilonorhynchus_violaceus Atrichornis_clamosus Menura_novaehollandiae Neodrepanis_coruscans Serilophus_lunatus Sapayoa_aenigma Pitta_sordida Calyptomena_viridis Smithornis_capensis Rhegmatorhina_hoffmannsi Sakesphorus_luctuosus Grallaria_varia Scytalopus_superciliaris Formicarius_rufipectus Sclerurus_mexicanus Furnarius_figulus Campylorhamphus_procurvoides Xiphorhynchus_elegans Lepidothrix_coronata Manacus_manacus Cephalopterus_ornatus Pachyramphus_minor Onychorhynchus_coronatus Oxyruncus_cristatus Piprites_chloris Neopipo_cinnamomea Tachuris_rubrigastra Mionectes_macconnelli Tyrannus_savana Eolophus_roseicapillus Amazona_guildingii Agapornis_roseicollis Bucorvus_abyssinicus Brachypteracias_leptosomus Eurystomus_gularis Todus_mexicanus Baryphthengus_martii Chloroceryle_aenea Bucco_capensis Galbula_dea Picoides_pubescens Psilopogon_haemacephalus Ramphastos_sulfuratus Semnornis_frantzii Ciccaba_nigrolineata Cathartes_aura Circaetus_pectoralis Haliaeetus_leucocephalus Aquila_chrysaetos Spizaetus_tyrannus Thalassarche_chlororhynchos Fregetta_grallaria Hydrobates_tethys Fulmarus_glacialis Ciconia_maguari Mesembrinibis_cayennensis Cochlearius_cochlearius Egretta_garzetta Balaeniceps_rex Scopus_umbretta Sula_dactylatra Anhinga_anhinga Anhinga_rufa Phalacrocorax_carbo Phalacrocorax_pelagicus Phalacrocorax_harrisi Phalacrocorax_auritus Phalacrocorax_brasilianus Nyctiprogne_leucopyga Antrostomus_carolinensis Chordeiles_acutipennis Nyctibius_bracteatus Nyctibius_grandis Podargus_strigoides Aegotheles_bennettii Chaetura_pelagica Hemiprocne_comata Burhinus_bistriatus Chionis_minor Pluvianellus_socialis Charadrius_alexandrinus Himantopus_himantopus Limosa_lapponica Arenaria_interpres Calidris_pugnax Pedionomus_torquatus Thinocorus_orbignyianus Jacana_jacana Nycticryphes_semicollaris Rostratula_benghalensis Turnix_velox Dromas_ardeola Glareola_pratincola Rhinoptilus_africanus Stercorarius_parasiticus Cepphus_grylle Uria_aalge Uria_lomvia Phaetusa_simplex Rynchops_niger Rissa_tridactyla Chroicocephalus_maculipennis Larus_smithsonianus Heliornis_fulica Psophia_crepitans Aramus_guarauna Balearica_regulorum Syrrhaptes_paradoxus Columbina_picui Columba_livia Centropus_unirufus Cuculus_canorus Ceuthmochares_aereus Piaya_cayana Apteryx_rowi Eudromia_elegans Nothoprocta_perdicaria Nothocercus_julius Nothocercus_nigrocapillus Crypturellus_soui Crypturellus_cinnamomeus Crypturellus_undulatus'

with open("chr1_namelist_random.txt") as f:
    f_list = f.readlines()

def run_mix123(tuple_list):   
    model, chrm, i = tuple_list
    
    if not os.path.exists('chr'+chrm+'_filtered3'):
        os.makedirs('chr'+chrm+'_filtered3')
    
        
    name = f_list[i].split(" ")[1].rstrip()    
    f_name = 'chr'+chrm+'/'+ name
    filtered_f_name = 'chr'+chrm+'_filtered3/'+ name + '-out.fas'
    if not os.path.isfile(filtered_f_name):
        filter_cmd = 'python3 AMAS.py remove -x ' + result_string + ' -d dna -f fasta -i ' + f_name + ' -u fasta -g chr'+chrm+'_filtered3/'
        os.system(filter_cmd)
    
    out_name = 'chr'+chrm+'_filtered3/'+str(i) + '_' + name

    cmd1 = '/usr/bin/time -v /home/remote/u7151703/software/iqtree-2.3.5.2.mf-Linux-intel/bin/iqtree2 -m MIX+MFP -mset GTR -mrate E,I,G,I+G -wspm -pre '+out_name+ ' -nt 1 -s ' + filtered_f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'a+') as f:
        #f.write(result.stdout)
        f.write(result.stderr)

def run_c1(tuple_list):   
    model, chrm, i = tuple_list
    
    if not os.path.exists('c1_chr'+chrm+'_filtered3'):
        os.makedirs('c1_chr'+chrm+'_filtered3')
    
        
    name = f_list[i].split(" ")[1].rstrip()    
    f_name = 'chr'+chrm+'/'+ name
    filtered_f_name = 'c1_chr'+chrm+'_filtered3/'+ name + '-out.fas'
    if not os.path.isfile(filtered_f_name):
        filter_cmd = 'python3 AMAS.py remove -x ' + result_string + ' -d dna -f fasta -i ' + f_name + ' -u fasta -g c1_chr'+chrm+'_filtered3/'
        os.system(filter_cmd)
    
    out_name = 'c1_chr'+chrm+'_filtered3/'+str(i) + '_' + name

    cmd1 = '/usr/bin/time -v /home/remote/u7151703/software/iqtree-2.3.5.2.mf-Linux-intel/bin/iqtree2 -m MFP -mset GTR -mrate E,I,G,I+G -pre '+out_name+ ' -nt 1 -s ' + filtered_f_name 
    result = subprocess.run(cmd1, shell=True, text=True, capture_output=True)
    with open(out_name + '_time.txt', 'a+') as f:
        #f.write(result.stdout)
        f.write(result.stderr)

def control(model, chrm, start, end, n_pool):
    if model not in ['mix123','c1']:
        print("wrong model type")
        sys.exit(1)
           
    start = int(start)
    chrm = str(chrm)
    end = int(end)
    n_pool = int(n_pool)
# =============================================================================
#     if model == 'aa_c20':
#         n_pool = int(n_pool/3)
# =============================================================================
    
    replicates = list(np.arange(start,end,1))
    
    tuple_list = ['']*len(replicates)

    for i in range(len(tuple_list)):
        tuple_list[i] = model, chrm, replicates[i]
        
    if model == 'mix123':
        partial_running = partial(run_mix123)
    elif model == 'c1':
        partial_running = partial(run_c1)
        
    with Pool(n_pool) as p:
        p.map(partial_running, tuple_list)

parser = argparse.ArgumentParser(description='')
parser.add_argument('--model', '-m', help='mix123',
                    required=True)
parser.add_argument('--chrm', '-c', help='',
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
        control(args.model, args.chrm,  args.start, args.end, args.n_pool)
    except Exception as e:
        print(e)

