from ete3 import Tree

gene_treefile = 'cds4/mixture.treefile'

gene_treestr = open(gene_treefile,'r').read()
gene_tree = Tree(gene_treestr)

    
species_treefile = 'exon_c12_unrooted.treefile'
species_treestr = open(species_treefile,'r').read()
species_tree = Tree(species_treestr,format=1)

taxa = set(gene_tree.get_leaf_names())
species_tree.prune(taxa)
species_tree.unroot()

pruned_tree = 'cds4/exon_c12_unrooted_pruned.treefile'
with open(pruned_tree, 'w+') as result:
    result.write(species_tree.write() + '\n')
    