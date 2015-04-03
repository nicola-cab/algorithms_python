from iterator import reverse_iterator #reverse iteration

class stack:
    """ class stack. hand crafted data structure made for study purposes"""
    
    def __init__(self):
        """ stack ctor: initialize empty stack """
        self.__list = []; 
        pass
        
    def push(self, element):
        """ add new item into stack"""
        self.__list.append(element)
    
    def pop(self):
        """ pop element from """
        if self.isEmpty() == False:
            return self.__list.pop()    
        raise Exception("buffer underflow") 
    
    def peek(self):
        """ return the top of the stack without removing the element"""
        if self.isEmpty() == False:
            return self.__list[len(self.__list)-1]
        raise Exception("buffer underflow")
        
    def isEmpty(self):
        """ returns true if the stack is empty """
        if not self.__list:
            return True 
        return False
    
    def size(self):
        """ return size of the stack"""
        return len(self.__list)
        
    def __iter__(self):
        """ iteration for stack"""
        it = reverse_iterator(self.__list)
        return it