from ete3 import Tree

def abbreviate_species_name(species_name):
    words = species_name.split('_')
    abbreviation = ''.join([word[:3].upper() for word in words])
    return abbreviation

candi_treefile = r'C:\Users\u7151703\OneDrive - Australian National University\Desktop\research\aves_evo\draft_results\exon200.treefile'
candi_treestr = open(candi_treefile,'r').read()
candi_tree = Tree(candi_treestr,format = 1)

        
ref_treefile = r'C:\Users\u7151703\OneDrive - Australian National University\Desktop\research\aves_evo\draft_results\63K.treefile'
ref_treestr = open(ref_treefile,'r').read()
ref_tree = Tree(ref_treestr,format = 1)

taxon_list_full = []
for n in ref_tree.traverse():
    if n.is_leaf():
        taxon_list_full.append(n.name)

taxon_list_short = [abbreviate_species_name(name) for name in taxon_list_full]

# checking ####
taxon_list = []
for n in candi_tree.traverse():
    if n.is_leaf():
        taxon_list.append(n.name)        

s_taxon_list = sorted(taxon_list) 
s_taxon_list_short = sorted(taxon_list_short)

for i in range(len(s_taxon_list)):
    if s_taxon_list_short[i] not in s_taxon_list:
        print(i+1)
################


# transfer short name to full name        
def find_taxon_name(name):
    index = taxon_list_short.index(name)
    return taxon_list_full[index]

for n in candi_tree.traverse():
    if n.is_leaf():
        if n.name in taxon_list_short:
            n.name = find_taxon_name(n.name)
        elif n.name == 'NANAUR':
            n.name = find_taxon_name('PHAAUR')
            print(1)
        elif n.name == 'NANBRA':
            n.name = find_taxon_name('PHABRA')
            print(2)
        elif n.name == 'NANHAR':
            n.name = find_taxon_name('PHAHAR')
            print(3)
        elif n.name == 'PORRUF':
            n.name = 'Pomatorhinus_ruficollis'
            print(4)
        elif n.name == 'POSRUF':
            n.name = 'Pomatostomus_ruficeps'
            print(5)
        elif n.name == 'URIPEL':
            n.name = find_taxon_name('PHAPEL')
            print(6)
        else:
            print('outlier!')
                
candi_tree.unroot()
with open(r'C:\Users\u7151703\OneDrive - Australian National University\Desktop\research\aves_evo\draft_results\exon200_unrooted.treefile', 'w+') as result:
    result.write(candi_tree.write(format = 1) + '\n')    


# transfer full name to short name   
def find_abb_name(name):
    index = taxon_list_full.index(name)
    return taxon_list_short[index]

for n in ref_tree.traverse():
    if n.is_leaf():
        if find_abb_name(n.name) in taxon_list:
            n.name = find_abb_name(n.name)
        elif find_abb_name(n.name) == 'PHAAUR':
            n.name = 'NANAUR'
            print(1)
        elif find_abb_name(n.name) == 'PHABRA':
            n.name = 'NANBRA'
            print(2)
        elif find_abb_name(n.name) == 'PHAHAR':
            n.name = 'NANHAR'
            print(3)
        elif n.name == 'Pomatorhinus_ruficollis':
            n.name = 'PORRUF'
            print(4)
        elif n.name == 'Pomatostomus_ruficeps':
            n.name = 'POSRUF'
            print(5)
        elif find_abb_name(n.name) == 'PHAPEL':
            n.name = 'URIPEL'
            print(6)
        else:
            print('outlier!')

ref_tree.unroot()
with open(r'C:\Users\u7151703\OneDrive - Australian National University\Desktop\research\aves_evo\draft_results\63K_unrooted.treefile', 'w+') as result:
    result.write(ref_tree.write(format = 1) + '\n')   
            
