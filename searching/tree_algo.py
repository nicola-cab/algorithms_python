#
#   In this script are reported the a bunch of common algorithm the could be needed playing with trees.
#   Note that these algorithms rely on tree_node data structure doing assumptions about its interal fields.
#   Methods may use recursion, then they are not good if you need extreme performances. 
#   Methods accept and return only tree_nodes
#

#tree walking. 
# pre-order  : 
# post-order : 
# in-order   : 
# level-order: (default used by all the trees implemented) 

def tree_visit_pre_order(node):
    if node == None:
        return

    print(node)
    tree_visit_pre_order(node.left)
    tree_visit_pre_order(node.right)

def tree_visit_post_order(node):
    if node == None:
        return 

    tree_visit_post_order(node.left)
    tree_visit_post_order(node.right)
    print(node)

def tree_visit_in_order(node):
    if node == None:
        return 

    tree_visit_in_order(node.left)
    print(node)
    tree_visit_in_order(node.right)

def tree_visit_level_order(node):
    """ tree level order is a possible application for bsf algorithm """
    


def tree_min(node):
    if node == None:
        raise Exception("node is null. Operation aborted")

    while node.left:
        node = node.left

    return node

def tree_max(node):
    if node == None:
        raise Exception("node is null. Operation aborted")

    while node.right:
        node = node.right

    return node

def tree_delete_min(node):
    if node == None:
        raise Exception("node is null. Operation aborted")

    return tree_delete_min_(node)

def tree_delete_min_(node):
    if node.left == None:
        return node.right
    node.left = tree_delete_min_(node.left)
    return node

