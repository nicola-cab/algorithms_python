import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )  

from base.iterator import iterator
from tree_algo import  bst_insert, bst_find, bst_delete, tree_visit_level_order

class rb_tree:
    """ 
        rb_tree implementation. 
        Balanced tree that guarantees log N performances for insert/find/delete
        In practise you may consider always if it is the worth to pay for a node based container rather to rely on simple
        vector of elements. Mostly depends if you want pay for a slower insertion in order to have a fast searching/ deletation
        In fact they are node based containers and they rely on pointers.
    """

    #static fields
    __red = 1
    __black = 0

    def __init__(self):
        self.root = None 
     
    def insert(self, key):
        if key == None:
            raise Exception("Key passed is not valid")
        
        self.root = bst_insert(self.root, key)
 
    def find(self, key):
        if key == None:
            raise Exception("Key passed is not valid")
        return bst_find(self.root, key)
             
    def delete(self):
        pass

    def __iter__(self):
        return iterator(tree_visit_tree_level(self.root))
