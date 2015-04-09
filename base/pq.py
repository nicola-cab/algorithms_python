from iterator import iterator
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
        it inits a index variable in order to insert into pq
        """
        #note: using a list could potentially slow down the delete operation due link operations after a deletation. Python has heappq
        self.__data  = [0] 
        self.__comparator = comparator
        self.__size     = 0
    
    def insert(self, elem):
        """ 
        insert into the priority queue accordingly with the comparator chosen.
        - realize min pq if keys are less equal to father's key
        - realize max pq if keys are greater equal to father's key
        """
        self.__size += 1 
        self.__data.append(elem)
        self.__insert_heapify(self.__size)

    
    def delElem(self):
        """ 
        delete from the priority queue accordingly with the comparator chosen.
        - delMin if the user selected to set up a min pq
        - delMax if the user selected to set up a max pq        
        """
        if self.isEmpty():
            raise Exception("Priority queue is empty")

        key = self.__data[1]
        self.__data[1] = self.__data[self.__size]
        self.__size -= 1
        self.__data.pop()
        self.__delete_heapify(1)
        
        return key
    
    def isEmpty(self):
        """ return true if the pq is empty"""
        return self.__size == 0
    
    def size(self):
        """ return number of elements """
        return self.__size
    
    def get(self):
        """ 
        return min element or max element for pq.
        - min is returned if user set up a min pq
        - max is returned if user set up a max pq
        """
        if self.isEmpty():
            raise Exception("Priority queue is empty")

        return self.__data[1] #indexes start from 1

    def __iter__(self):
        """ iterate through priority queueu using iterator utility """
        return iterator(self.__data[1:])
    
    ######################
    #  utilities methods #
    ######################
    
    def __insert_heapify(self, k):
        """
            Insert could create keys unbalancing in the tree..
            Coping with this situation  means:
            -1 exchange key of the child with parent (swimming for leaves to root)
            -2 continue till heap is not 'heapified' again
        """
        while k>1 and self.__comparator(self.__data[k], self.__data[k//2]):
            #swap keys - swim up in order to get the root of the tree
            self.__data[k], self.__data[k//2] = self.__data[k//2], self.__data[k]
            k = k//2

    def __delete_heapify(self, k):
        """ 
            delete introduce a potentially need to rebalance the tree.
            In this case it is needed walk through the tree or subtrees and heapify it:
            Algorithm explanation:
            - sink through the tree till end is reached.
            - find a key that is breaking the heap (it depends if is min or max heap)
            - perform a cmp between father and the child's key
            - swap them only if heap property is violated.
        """
        N = self.__size
        while 2*k <= N:
            j = 2*k

            #little tip:
            #
            # using a generic comparator allowed me to save lines of code.. but the cost to pay is that 
            # a rule must be followed, infact the comparator is not commutative since the priority queue
            # must follow a strict ordering. Than operands a and b (relation is not symmetric) cannot be swapped. 
            # This is perfectly legal, since you'd never swap a and b seeing this ' if a < b: '.
            # The big flaw of this approach is that comparator does not have any information about the operation that 
            # it is implementing, then programmers cannot read this code and understand immediately what it is doing.
            #
            # the rule for thumb should be to think about the comparator passed and translate it in the equivalent math symbol.
            # for example:
            #
            #   less_comparator(a, b)   -->  a<b ? True: False
            #   
            # In this case the firs if it's just checking for the lower key between two children. at saving its index in j. 
            # Index j is used to compare child's key with father key using the same comparator and understand if father and 
            # and child must be swapped. The process is related until father's key is lower than child's key.
            #
            if j<N and self.__comparator(self.__data[j+1], self.__data[j]): 
                j+=1
            if(not self.__comparator(self.__data[j],self.__data[k])):
                break
            self.__data[k], self.__data[j] = self.__data[j], self.__data[k]
            k = j




