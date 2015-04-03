class iterator:
    """ iterators are useful objects that could be used to walk through a collection """
    def __init__(self, data):
        self.__data  = data
        self.__index = 0
        self.__len   = len(self.__data)
    
    def __iter__(self):
        return self
    
    def __next__(self): #note in python 2.x should be next
        if self.__index == self.__len:
            raise StopIteration
        elem = self.__data[self.__index]
        self.__index = self.__index + 1
        return elem 

class reverse_iterator:
    """ sometimes could be useful scroll even in the opposite direction"""
    def __init__(self,data):
        self.__data = data
        self.__index = len(self.__data)
    
    def __iter__(self):
        return self
    
    def __next__(self): #note in python 2.x should be next
        if self.__index == 0:
            raise StopIteration
        self.__index = self.__index -1
        return self.__data[self.__index]
