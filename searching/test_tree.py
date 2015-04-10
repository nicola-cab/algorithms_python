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

    bst.delete(4)
    print("Find."   ,bst.find(1))
    print("Find."   ,bst.find(5))

 
if __name__ == "__main__":

    #fix imports because I am using some utility from other packages
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

    from sorting.utils import generate
    from bst import bst_tree

    test_bst_tree()
