import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) ) 

from base.iterator import iterator

class bucket:
    def __init__(self):
        self.bucket = []

    def add(self,key):
        if key == None:
            raise Exception("Key value is None")
        self.bucket.append(key)

    def get(self, key):
        if key == None:
            raise Exception("key value is None")
        for item in self.bucket:
            if item == key:
                return item
        return None

    def delete(self, key):
        if key == None:
            raise Exception("key value is None")
        self.bucket.remove(key)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.bucket)

    def __iter__(self):
        return iterator(self.bucket)

class linear_chain_hash_map:
    """
        Hash map representation using chaining technique for conflict resolution.
        This class uses hash python built in function, which uses the __hash__ function
        for each object passed to it.
    """

    def __init__(self, m):
        self.n = 0  # number of keys
        self.m = m  #number of bins
        self.hash_map = []
        for i in range(m):
            self.hash_map.append(bucket())  

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.n

    def contains(self, key):
        if key == None:
            raise Exception("Invalid key")

        return self.get(key) != None

    def get(self, key):
        i = self.__hash_function__(key)
        return self.hash_map[i].get(key)

    def put(self, key):
        if key == None:
            raise Exception("Invalid key")

        #cope with reallocation

        if not self.contains(key):
            i = self.__hash_function__(key)
            self.hash_map[i].add(key)
            self.n += 1

    def delete(self, key):
        if key == None:
            raise Exception("Invalid key")

        if self.contains(key):
            i = self.__hash_function__(key)
            self.hash_map[i].delete(key)
            self.n -= 1

        #cope with reallocation

    def __iter__(self):
        list = []
        i = 0
        for bucket in self.hash_map:
            for item in bucket:
                list.append(item)
        return iterator(list)
        
    def __hash_function__(self,key):
        return (hash(key) & 0x7fffffff) % self.m

    def __resize__(self, m):
        tmp_hash_map = linear_chain_hash_map(m) 



if __name__ == "__main__":

    hash_map = linear_chain_hash_map(10)
    list = [10, 9,6,11,1,3,2,2,6,7,12,13]
    for i in list:
        hash_map.put(i)

    print("Hash map size =", hash_map.size())
    
    print("Print Hash map:")
    for key in hash_map:
        print("key = ", key)

    print("Delete 2")
    hash_map.delete(2)

    print("Print Hash Map")
    for key in hash_map:
        print("key = ", key)


