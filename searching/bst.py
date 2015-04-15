import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) ) 

from tree_node import tree_node
from base.iterator import iterator
from tree_algo import  tree_visit_level_order, tree_min, tree_delete_min, tree_size

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
        self.root = self.__bst_insert( self.root, key )
    
    def find(self, key):
        if key == None:
            raise Excpetion("Key is not valid. operation aborted")
        return  self.__bst_find(self.root, key)
    
    def delete(self,key):
        if key == None:
            raise Excpetion("Key is not valid. operation aborted")
        self.root = self.__bst_delete(self.root, key)

    def __iter__(self):
        return iterator(tree_visit_level_order(self.root))

    #
    # private bst implementation
    #
    def __bst_insert(self, node, key):
        if node == None:
            node = tree_node(key)
            node.count = 1
            return node
        else:
            if key<node.key:
                node.left = self.__bst_insert(node.left, key)
            elif key>node.key:
                node.right = self.__bst_insert(node.right, key)
            else:
                node.key = key #duplication not allowed. this is a simple set
        
            node.count = tree_size(node.left) + tree_size(node.right) + 1
            return node

    def __bst_find(self, node, key):
        if node == None:
            raise Exception("error key not found")
    
        if node.key == key:
            return key
        elif key<node.key:
            return self.__bst_find(node.left, key)
        else:
            return self.__bst_find(node.right, key)

    def __bst_delete(self, node, key):
    
        if node == None:
            raise Exception("error key not found")
    
        if key < node.key:
            node.left = self.__bst_delete(node.left, key)
        elif key > node.key:
            node.right = self.__bst_delete(node.right, key)
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
