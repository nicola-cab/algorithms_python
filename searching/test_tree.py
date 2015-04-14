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
    from tree_algo import tree_floor, tree_ceiling

    test_bst_tree()
