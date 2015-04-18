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
#   find element bst
#
def bst_find(node, key):
    if node == None:
        raise Exception("error key not found")     
    if node.key == key: return key
    elif key<node.key:  return bst_find(node.left, key)
    else:               return bst_find(node.right, key)

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
    if n == None:   raise Exception("k-th key non found in tree. is k-th element into tree's keys range?")
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

#
# Rotation for balanced trees
#

def tree_rotate_left(h):
    x = h.right
    h.right = x.left
    x.left  = h

    x.color = h.color
    h.color = 1 #red
    x.count = h.count
    h.count = 1 + tree_size(h.left) +  tree_size(h.right)
    h.height = tree_compute_height(h)
    x.height = tree_compute_height(x)
    return x

def tree_rotate_right(h):
    x = h.left
    h.left = x.right
    x.right = h

    x.color = h.color
    h.color = 1 #red
    x.count = h.count
    h.count = 1 + tree_size(h.left) +  tree_size(h.right)
    h.height = tree_compute_height(h)
    x.height = tree_compute_height(x)
    return x

def tree_balance_check(node):
    """ 
        Tree algorithm used in avl trees in order to understand if rotations are needed.
        Assumption of this method are:
            -1 bst node is provided
            -2 field height is present in the node object
        Important difference between left subtree and right subtree mustn't be up to 2.
    """
    if node == None:
        return 0
    if node.left == None:
        left_h = 0          
    else: 
        left_h = 1 + node.left.height
    if node.right == None:
         right_h = 0
    else: 
        right_h = 1 + node.right.height 
    return left_h - right_h

def tree_compute_height(node):
    if node == None:
        return 0
    if node.left == None and node.right == None:
        return 0
    if node.left == None and node.right:
        return 1 + node.right.height
    if node.left and node.right == None:
        return 1 + node.left.height
    return max(node.left.height, node.right.height) + 1
