import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) ) 

from tree_node import tree_node
from base.iterator import iterator
from tree_algo import  tree_visit_level_order, tree_min, tree_delete_min, bst_find
from tree_algo import tree_rotate_left, tree_rotate_right, tree_compute_height, tree_balance_check, tree_size

class avl_tree:
    """
        Implementation for avl binary search tree.
        The avl binary search tree is binary tree that guarantees lg N time for insert/find/delete.
        The avl tree use rotation coupled with height analysis between nodes in order to accomplish balancing
        
        Important:
            - this implementation uses massively recursion. 
            - Probably in practise you will never want use heavy recursive algorithms
    """
   
    def __init__(self):
         self.root = None
         
    def __str__(self):
        return "avl tree"
    
    def insert(self, key):
        if key == None:
            raise Excpetion("Key is not valid. operation aborted")
        self.root = self.__avl_insert(self.root, key)
                                 
    def find(self, key):
        if key == None:
            raise Excpetion("Key is not valid. operation aborted")
        return  bst_find(self.root, key)     
                                             
    def delete(self,key):
        if key == None:
            raise Excpetion("Key is not valid. operation aborted")
        if self.root == None:
            raise Exception("Tree is empty")
        self.root = self.__avl_delete(self.root, key)
        pass

    def __iter__(self):
        return iterator(tree_visit_level_order(self.root))
    
    #
    #   private utilis methods for avl tree
    #

    def __avl_insert(self, node, key):
        
        if node == None:
            n = tree_node(key)
            n.count = 1
            return n
        if key < node.key:
            node.left = self.__avl_insert(node.left, key)
            height = tree_balance_check(node)
            if height == 2:
                if key < node.left.key:
                    node = self.__ll_rotation(node)
                else:
                    node = self.__lr_rotation(node)
        elif key > node.key:
            node.right = self.__avl_insert(node.right, key)
            height = tree_compute_height(node)
            if height == -2:
                if key < node.right.key:
                    node = self.__rl_rotatation(node)
                else:
                    node = self.__rr_rotations(node)
        else:
            node.key = key

        node.height = tree_compute_height(node)
        node.count = tree_size(node.left) + tree_size(node.right) + 1

        return node

    def __avl_delete(self, node, key):
        #like bst deletation + rebalacing stuff
        if key < node.key:
            node.left = self.__avl_delete(node.left, key)
            h = tree_balance_check(node)
            if h == -2:
                if tree_balance_check(node.right) <= 0:
                    node = self.__rr_rotations(node)
                else:
                    node = self.__rl_rotatation(node)
        elif key > node.key:
            node.right = self.__avl_delete(node.right, key)
            h = tree_balance_check(node)
            if h == 2:
                if tree_balance_check(node.left) <= 0:
                    node = self.__ll_rotation(node)
                else:
                    node = self.__lr_rotation(node)
        else:
            #equal to std bst deletation
            if node.left == None:
                return node.right
            if node.right == None:
                return node.left

            t = node
            node = tree_min(t.right)
            node.right = tree_delete_min(t.right)
            node.left = t.left
            node.count = tree_size(node.left) + tree_size(node.right) + 1
            node.height = tree_compute_height(node)

            return node

    def __ll_rotation(self, node):
        node = tree_rotate_right(node)
        return node
    
    def __lr_rotation(self, node):
        node.left = tree_rotate_left(node.left)
        node = tree_rotate_right(node)
        return node

    def __rl_rotatation(self, node):
        node.right = tree_rotate_right(node.right)
        node = tree_rotate_left(node)
        return node

    def __rr_rotations(self, node):
        node = tree_rotate_left(node)
        return node
