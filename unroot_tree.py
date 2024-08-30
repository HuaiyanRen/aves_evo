from ete3 import Tree

true_treefile = r'C:\Users\u7151703\OneDrive - Australian National University\Desktop\aa100.treefile'
true_treestr = open(true_treefile,'r').read()

true_tree = Tree(true_treestr,format = 1)
true_tree.unroot()
with open(r'C:\Users\u7151703\OneDrive - Australian National University\Desktop\aa100_unrooted.treefile', 'w+') as result:
    result.write(true_tree.write(format = 1) + '\n')    



# =============================================================================
# gcf_list = []
# for n in true_tree.traverse():
#     if not n.is_leaf():
#         if n.name != '':
#             gcf_list.append(float(n.name))
# =============================================================================
