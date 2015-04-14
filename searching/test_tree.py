def test_bst_tree():
    print("test bst")

    values = [4,1,5]
    print(values)  

    bst = bst_tree()
    for v in values:
        bst.insert(v)

    try:
        bst.find(10)
    except:
        print("Ops value not found")

    print( bst.find(4) )
    print("Find."   ,bst.find(1))
    print("Find."   ,bst.find(5))

    print("visit in order")
    tree_visit_in_order(bst.root)
    print("visit in pre order")
    tree_visit_pre_order(bst.root)
    print("visit in post order")
    tree_visit_post_order(bst.root)
    print("Visit level order")
    for i in bst:
        print(i)

    print("Delete 4")
    bst.delete(4)
    print("Visit level order")
    for i in bst:
        print(i)

    bst.insert(4)
    bst.insert(7)

    print("Visit level order")
    for i in bst:
        print(i)

    print("Floor")
    print(tree_floor(bst.root,2))

    print("Ceiling")
    print(tree_ceiling(bst.root,2))
    
    print("Rank. Number of keys that have at least 2 children.. in this tree only one")
    print(tree_rank(bst.root, 2))
    
    print("Select the k-th item in the tree ... ")
    print("Min is = ", tree_select(bst.root, 0))
    print("Median is = ",tree_select(bst.root, len(values)//2))
    print("Max is =",tree_select(bst.root, 3))
    
    if tree_min(bst.root) == tree_select(bst.root,0):
        raise Exception("Test failed min not equal to select 0-th element")
    else:
        print("min <-> select test passed ")
        
    if tree_max(bst.root) == tree_select(bst.root,3):
        raise Exception("Test failed max not equal to select 3-th element")
    else:
        print("max <-> select test passed ")
   
if __name__ == "__main__":

    #fix imports because I am using some utility from other packages
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

    from sorting.utils import generate
    from bst import bst_tree

    #tree visits
    from tree_algo import tree_visit_in_order, tree_visit_pre_order, tree_visit_post_order, tree_visit_level_order

    #tree statistc orders
    from tree_algo import tree_min, tree_max, tree_floor, tree_ceiling, tree_rank, tree_select

    test_bst_tree()
