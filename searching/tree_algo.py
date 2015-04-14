#
#   In this script are reported the a bunch of common algorithm the could be needed playing with trees.
#   Note that these algorithms rely on tree_node data structure doing assumptions about its interal fields.
#   Methods may use recursion, then they are not good if you need extreme performances. 
#   Methods accept and return only tree_nodes
#

from tree_node import tree_node

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
    """ 
        tree level order is a possible application for bsf algorithm. 
        BSF is partially implemented since I don't really need to mark
        nodes. In bst I don't have cycles and only 2 possible path per node.
        A list of nodes ordered by level is returned.
    """
    q = [node]
    res = []
    while q:
        l = list()
        for x in q:
            res.append(x)
            if x.left: l.append(x.left)
            if x.right: l.append(x.right)
        q = l

    return res

#
#   insert/find/delete for generic bst
#

def bst_insert(node, key):
    if node == None:
        node = tree_node(key)
        node.count = 1
        return node
    else:
        if key<node.key:
            node.left = bst_insert(node.left, key)
        elif key>node.key:
            node.right = bst_insert(node.right, key)
        else:
            node.key = key #duplication not allowed. this is a simple set
            
        node.count = tree_size(node.left) + tree_size(node.right) + 1
        return node

#
#   find in bst
#
def bst_find(node, key):
    if node == None:
        raise Exception("error key not found")
    
    if node.key == key:
        return key
    elif key<node.key:
        return bst_find(node.left, key)
    else:
        return bst_find(node.right, key)

#
#   delete for bst
#
def bst_delete(node, key):

    if node == None:
        raise Exception("error key not found")

    if key < node.key:
        node.left = bst_delete(node.left, key)
    elif key > node.key:
        node.right = bst_delete(node.right, key)
    else:
        #found item to delete
        
        #cope with single child or no children
        if node.left == None:
            return node.right
        if node.right == None:
            return node.left
        
        #two children.
        # the min element in right subtree for key must become the new root of
        # the subtree
            
        t = node
        node = tree_min(t.right)              #substitute the root for the subtree
        node.right = tree_delete_min(t.right) #delete the min because it is going to be the new root for subtree
        node.left = t.left                    #set left subtree
            
        return node

#
#   delete min in bst
#
def tree_delete_min(node):
    if node == None:
        raise Exception("node is null. Operation aborted")
        
    return tree_delete_min_(node)

def tree_delete_min_(node):
    if node.left == None:
        return node.right
    node.left = tree_delete_min_(node.left)
    return node

#
#   get keys rooted by node
#
def tree_size(node):
    if node:
        return node.count
    return 0
    
#
#   Order statistics for bst.
#       Methods accept a pair composed by node and key and return a node.
#

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

def tree_floor(node, key):
    """ The largest key <= a given key -- alas lower bound"""
    if node == None or key == None:
        raise Exception("node is null or key is not valid. Operation aborted")
    n = tree_floor_(node, key)
    if n == None:   raise Exception("floor not found")
    return n.key

def tree_ceiling(node, key):
    """ Smallest key >= a given key -- alas upper_bound"""
    if node == None or key == None:
        raise Exception("node is null or key is not valid. Operation aborted")    
    n = tree_ceiling_(node, key)
    if n == None: raise Exception("ceiling not found")
    return n.key

def tree_rank(node, k):
    """ Number of key <= k """
    if node == None or k == None:
        raise Exception("node is null or key is not valid. Operation aborted")
    return tree_rank_(node, k)

def tree_select(node, k):
    """ select the k-th key in tree (like quick_select) """
    if node == None or k == None:
        raise Exception("node is null or key is not valid. Operation aborted")
    n = tree_select_(node, k)
    if n == None:   raise Exception("Bad error, bug in algorithm")
    return n.key
    
#
# Recursive implementation for some tree_algo functions
#
def tree_floor_(node, key):
    if node == None:     return node
    if node.key == key:  return node
    if key < node.key:   return tree_floor_(node.left, key)
    t = tree_floor_(node.right, key)
    if t != None: return t
    else: return node

def tree_ceiling_(node, key):
    if node == None:    return node
    if node.key == key: return node
    if key > node.key:  return tree_ceiling_(node.right, key)
    t = tree_ceiling_(node.left, key)
    if t != None: return t
    else: return node

def tree_rank_(node, k):
    if node == None:    return 0
    if k < node.key:  return tree_rank_(node.left, k)
    elif k > node.key:  return 1 + tree_size(node.left) + tree_rank_(node.right, k)
    else: return tree_size(node.left)

def tree_select_(node, k):
    if node == None: return None
    s = tree_size(node.left)
    if s > k:   return tree_select_(node.left, k)
    elif s < k: return tree_select_(node.right, k-s-1)
    else: return node
