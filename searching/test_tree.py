def test_tree(tree):
    print("test: ", tree)

    values = [4,1,5]
    print(values)  

    for v in values:
        tree.insert(v)

    try:
        tree.find(10)
    except:
        print("Ops 10 is not found")

    print( "Value found = ", tree.find(4) )
    print("Find."   ,tree.find(1))
    print("Find."   ,tree.find(5))

    print("visit in order")
    tree_visit_in_order(tree.root)
    print("visit in pre order")
    tree_visit_pre_order(tree.root)
    print("visit in post order")
    tree_visit_post_order(tree.root)
    print("Visit level order")
    for i in tree:
        print(i)

    print("Delete 4")
    tree.delete(4)
    print("Visit level order")
    for i in tree:
        print(i)

    tree.insert(4)
    tree.insert(7)

    print("Find 7 in tree success = ", tree.find(7) == 7  )

    print("Visit level order")
    for i in tree:
        print(i)

    print("Floor")
    print(tree_floor(tree.root,2))

    print("Ceiling")
    print(tree_ceiling(tree.root,2))
    
    print("Rank. Number of keys that are rooting a subtree composed by 2 children.. in this tree only one")
    print(tree_rank(tree.root, 2))
    
    print("Select the k-th item in the tree ... ")
    print("Min is = ", tree_select(tree.root, 0))
    print("Median is = ",tree_select(tree.root, len(values)//2))
    print("Max is =",tree_select(tree.root, 3))
    
    if tree_min(tree.root) == tree_select(tree.root,0):
        raise Exception("Test failed min not equal to select 0-th element")
    else:
        print("min <-> select test passed ")
        
    if tree_max(tree.root) == tree_select(tree.root,3):
        raise Exception("Test failed max not equal to select 3-th element")
    else:
        print("max <-> select test passed ")
        
    print("Check if the tree is a bst ")
    print(is_bst_tree(tree.root))
    
    if tree.__strt__() == "red black tree":
        print("Check if tree is rb tree ")
        print(is_23_tree(tree.root))

#
# Utility functions to test if tree is bst or 23 tree
#

def is_bst_tree(node):
    return is_bst(node, None, None)

def is_bst(node, min_key, max_key):
    if node == None:    return True
    if min_key != None and node.key <= min_key: return False
    if max_key != None and node.key >= max_key: return False
    return is_bst(node.left, min_key, node.key) and is_bst(node.right, node.key, max_key)

def is_23_tree(tree,node)
    return True 
    #return is_23(tree,node)

#def is_23(tree,node):
#    if node == None:    return True
#    if tree.isRed(node.right): return False
#    if node != tree.root:
   
if __name__ == "__main__":

    #fix imports because I am using some utility from other packages
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

    from sorting.utils import generate
    from bst import bst_tree
    from rb_tree import rb_tree

    #tree visits
    from tree_algo import tree_visit_in_order, tree_visit_pre_order, tree_visit_post_order, tree_visit_level_order

    #tree statistc orders
    from tree_algo import tree_min, tree_max, tree_floor, tree_ceiling, tree_rank, tree_select

    bst = bst_tree()
    rb_tree = rb_tree()

    #testing bst
    print("---------------------")
    test_tree( bst )
    #testing rb_tree
    print("----------------------")
    test_tree( rb_tree )
