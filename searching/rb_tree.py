import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )  

from tree_node import tree_node
from base.iterator import iterator
from tree_algo import bst_find, tree_visit_level_order, tree_size 
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
        return "red black tree implementation"
 
    def insert(self, key):
        if key == None:
            raise Exception("Key passed is not valid")
        self.root = self.rb_tree_insert(self.root, key)        
 
    def find(self, key):
        if key == None:
            raise Exception("Key passed is not valid")
        return bst_find(self.root, key)
             
    def delete(self, key):
        pass

    def __iter__(self):
        return iterator(tree_visit_level_order(self.root))

    #
    # rb tree internal algorithms to insert and delete node
    #

    def isRed( self, node):
        if node == None: return False
        return node.color == 1

    def flipColor(self, node):
        if node == None:
            return
        node.color = 1
        node.left.color = 0
        node.right.color = 0

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
