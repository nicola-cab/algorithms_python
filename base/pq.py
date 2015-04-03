from collections import deque
class pq:
    """ 
        Priority queue implementation.
        Priority queue have a broad range of applications (sorting, graphs, etc.)
        
        Properties of pq is that every key is less than father's key, in this case
        we refer to minimum priority queues (or min heap) otherwise if keys are greater than father's
        key we have maximum priority queue (or max heap).
    """
    
    def __init__(self, comparator):
        """ 
        ctor for my priority queue. it takes:
        -1 the data to process
        -2 the order of the keys to apply
        """
        self.__data  = deque([])
        self.__comparator = comparator
    
    def insert(self, elem):
        """ 
        insert into the priority queue accordingly with the comparator chosen.
        - realize min pq if keys must be less equal to father's one
        - realize max pq if keys must be less equal to father's one
        """
        pass
    
    def delElem(self):
        """ 
        delete from the priority queue accordingly with the comparator chosen.
        - delMin if the user selected to set up a min pq
        - delMax if the user selected to set up a max pq        
        """
        pass
    
    def isEmpty(self):
        """ return true if the pq is empty"""
        if not self.__data:
            return True
        return False
    
    def size(self):
        """ return number of elements """
        return len(self.__data)
    
    def get(self):
        """ 
        return min element or max element for pq.
        - min is returned if user set up a min pq
        - max is returned if user set up a max pq
        """
        return self.__data[1] #indexes start from 1
    
    ######################
    #  utilities methods #
    ######################
    
    def __swim(self, k):
        """ 
            this method solve the scenario in which the key becomes greater than father's one.
            Eliminating the variation means:
            -1 exchange key of the child with parent
            -2 continue till heap is not ok
        """
        
        while k>1 and 