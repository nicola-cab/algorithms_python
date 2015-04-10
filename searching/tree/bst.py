from tree_node import tree_node

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
    
    tree_node root
    
    def __init__(self):
        root = None
    
    def insert(self, key):
        self.root = self.__insert( root, key )
    
    def find(self, key):
        pass
    
    def delete(self,key):
        pass
        
    def __insert(self, node, key):
        if node == None:
            node = tree_node(key)
            return node
        else:
            if key<node.key:
                node.left = self.__insert(node.left, key)
            elif key>node.key:
                node.right = self.__insert(node.right, key)
            else:
                node.key = key #duplication not allowed. this is a simple set