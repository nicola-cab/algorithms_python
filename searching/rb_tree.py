import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )  

from tree_node import tree_node
from base.iterator import iterator
from tree_algo import bst_find, tree_visit_level_order, tree_size, tree_min, tree_delete_min 
from tree_algo import tree_rotate_left, tree_rotate_right

class rb_tree:
    """ 
        rb_tree implementation. 
        Balanced tree that guarantees log N performances for insert/find/delete
        In practise you may consider always if it is the worth to pay for a node based container rather to rely on simple
        vector of elements. Mostly depends if you want pay for a slower insertion in order to have a fast searching/ deletation
        In fact they are node based containers and they rely on pointers.
    """

    # 0 is black node
    # 1 is red node

    def __init__(self):
        self.root = None 

    def __str__(self):
        return "red black tree"
 
    def insert(self, key):
        if key == None:
            raise Exception("Key passed is not valid")
        self.root = self.rb_tree_insert(self.root, key)        
 
    def find(self, key):
        if key == None:
            raise Exception("Key passed is not valid")
        return bst_find(self.root, key)
             
    def delete(self, key):
        if key == None:
            raise Exception("Key passed is not valid")
        if self.root == None:
            raise Exception("Tree is empty")

        bst_find( self.root, key )

        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = 1 #make node red 

        self.root = self.rb_tree_delete(self.root, key)

    def __iter__(self):
        return iterator(tree_visit_level_order(self.root))

    #
    # rb tree internal algorithms to insert and delete node
    #

    def rb_tree_insert(self, node, key):
        """ Implementation for red black tree insertion. """

        if node == None:
            n = tree_node(key)
            n.count = 1 #number of nodes rooted is equal 1
            n.color = 1 #color is red
            return n
        
        if key < node.key: 
            node.left = self.rb_tree_insert(node.left, key)
        elif key > node.key: 
            node.right = self.rb_tree_insert(node.right, key)
        else:
            node.key = key

        # 
        #   balancing
        #
        if self.isRed(node.right) and not self.isRed(node.left):
            node = tree_rotate_left(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = tree_rotate_right(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColor(node)

        node.count = tree_size(node.left) + tree_size(node.right) + 1
        return node

    def rb_tree_delete(self, node, key):
        """
            Implementation for rb tree deletation.
            Basically binary tree deletation +
            rebalancing to keep rb tree invariants
        """
        if key < node.key:
            if not self.isRed(node.left) and not self.isRed(node.left.left):
                node = self.__move_red_left(node)
            node.left = self.rb_tree_delete(node.left, key)
        else:
            if self.isRed(node.left):
                node = tree_rotate_right(node)
            if key == node.key and node.right == None:
                return None
            if not self.isRed(node.right) and not self.isRed(node.right.left):
                node = self.__move_red_right(node)
            if node.key == key:
                x = tree_min(node.right)
                node.key = x.key
                node.right = tree_delete_min(node.right)
            else:
                node.right = self.rb_tree_delete(node.right, key)

        return self.__balance(node)

    #
    #   Utility functions. private use only
    #
    def __move_red_left(self, node):
        """ 
            Assuming that node is red and both node.left and node.left.left are both black.
            make h.left or one of it's children red
        """
        self.flipColor(node)
        if self.isRed(node.right.left):
            node.right = tree_rotate_right(node.right)
            node = tree_rotate_left(node)
            self.flipColor(node)
        return node

    def __move_red_right(self, node):
        """ 
            Assuming that node is red and both node.left and node.left.left are both black.
            make h.right or one of it's children red
        """
        self.flipColor(node)
        if self.isRed(node.left.left):
            node = tree_rotate_right(node)
            self.flipColor(node)
        return node
 
    def isRed( self, node):
        """ Check if node's color is red """
        if node == None: return False
        return node.color == 1

    def flipColor(self, node):
        """ Flip colors of current node """
        if node == None:
            return
        node.color = not node.color
        node.left.color = not node.right.color
        node.right.color = not node.right.color
    
    def __balance(self,node):
        """ Balance red black tree """
        if self.isRed(node.right):  
            node = tree_rotate_left(node)
        if self.isRed(node.left) and self.isRed(node.left.left): 
            node=tree_rotate_right(node)   
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColor(node)
        node.count = tree_size(node.left) + tree_size(node.right) + 1
        return node
