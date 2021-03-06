class tree_node:
    """ 
        Representation object for a generic node in a tree.
        Note that same fields may not be used by certain trees.
        In this class you will find color property (used by rb trees)
        or height (used by avl trees).
        Then the main drawback here is the space occupied by some field even though
        it is not used by certain implementations.
    """
    
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None
        self.color = 0  #0 is black 1 is red
        self.count  = 0 #number of nodes rooted
        self.height = 0 #height of the sub-tree rooted

    def __str__(self):
        return str(self.key)
