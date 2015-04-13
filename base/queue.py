from collections import deque
from iterator import iterator
class queue:
    """ 
        - hand crafted data structure made for study purposes.
        - accordingly with python documentation using list to implement a 
          queue is not a good choice for pop operation, since items must shifted
    """
    
    def __init__(self):
        """ queue ctor"""
        self.__list = deque([])
    
    def enqueue(self, elem):
        """ put new element in queue """
        self.__list.append(elem)
    
    def dequeue(self):
        """ remove element from queue """
        if self.isEmpty() == True:
            raise Exception("queue underflow")
        return self.__list.popleft()
        
    def last(self):
        """ return the last element in the queue without removing it"""
        if self.isEmpty() == True:
            raise Exception("queue underflow")
        return self.__list[0]
    
    def isEmpty(self):
        """ return true is the queue is empty """
        if not self.__list: 
            return True
        return False
    
    def size(self):
        """ return size of the queue"""
        return len(self.__list)
        
    def __iter__(self):
        """ iteration for stack"""
        it = iterator(self.__list)
        return it
