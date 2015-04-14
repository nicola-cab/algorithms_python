import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) ) 

from base.iterator import iterator
from tree_algo import  bst_insert, bst_find, bst_delete, tree_visit_level_order

class bst_tree:
    """
        Implementation for binary search tree.
        The bst does not guarantee any time complexity less than N to insert a key or remove one.
        The real structure of the tree depends by the order in which the keys are inserted. 
        
        Important:
            - this implementation uses massively recursion. 
            - Probably in practise you will never need this stuff
        
        Important:
            - this tree implements a set, there is not key/value organization.
            - this tree offers a level visit in case of iteration
    """
     
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if key == None:
            raise Excpetion("Key is not valid. operation aborted")
        self.root = bst_insert( self.root, key )
    
    def find(self, key):
        if key == None:
            raise Excpetion("Key is not valid. operation aborted")
        return  bst_find(self.root, key)
    
    def delete(self,key):
        if key == None:
            raise Excpetion("Key is not valid. operation aborted")
        self.root = bst_delete(self.root, key)

    def __iter__(self):
        return iterator(tree_visit_level_order(self.root))
