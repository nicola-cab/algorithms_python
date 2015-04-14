import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) ) 

from base.iterator import iterator
from tree_node import tree_node
from tree_algo import tree_min, tree_delete_min, tree_visit_level_order, tree_size

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
        self.root = self.__insert( self.root, key )
    
    def find(self, key):
        return self.__find(self.root, key)
    
    def delete(self,key):
        self.root = self.__delete(self.root, key)

    def __iter__(self):
        return iterator(tree_visit_level_order(self.root))

    def __insert(self, node, key):
        if node == None:
            node = tree_node(key)
            node.count = 1
            return node
        else:
            if key<node.key:
                node.left = self.__insert(node.left, key)
            elif key>node.key:
                node.right = self.__insert(node.right, key)
            else:
                node.key = key #duplication not allowed. this is a simple set
            
            node.count = tree_size(node.left) + tree_size(node.right) + 1
            return node

    def __find(self, node, key):
        if node == None:
            raise Exception("error key not found")

        if node.key == key:
            return key
        elif key<node.key:
            return self.__find(node.left, key)
        else:
            return self.__find(node.right, key)

    def __delete(self, node, key):

        if node == None:
            raise Exception("error key not found")

        if key < node.key:
            node.left = self.__delete(node.left, key)
        elif key > node.key:
            node.right = self.__delete(node.right, key)
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



