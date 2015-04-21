import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) ) 

from base.iterator import iterator

class probing_hash_map:
    """ 
        Hash map implementing probing technique to resolve conflicts 
    """

    def __init__(self,m):
        self.m = m
        self.n = 0
        self.hash_map = m*[None]

    def is_empty(self):
        return self.size == 0

    def size(self):
        return len(self.hash_map)

    def contains(self, key):
        if key == None:
            raise Exception("key is none!")
        return self.get(key) != None

    def get(self, key):
        i = self.__hash_function__(key)
        while self.hash_map[i] != None:
            if self.hash_map[i] == key:
                return self.hash_map[i]
            i = (i + 1) % self.m 
        return None

    def put(self, key):
        if key == None:
            raise Exception("key is none!")

        if self.n >= self.m//2:
            self.__resize__(self.m*2)

        i = self.__hash_function__(key)
        while self.hash_map[i] != None:
            if self.hash_map[i] == key:
                return 
            i = (i + 1) % self.m

        self.hash_map[i] = key
        self.n += 1

    def delete(self, key):
        if self.contains(key) == False:
            raise Exception("Key not found")

        i = self.__hash_function__(key)
        while key != self.hash_map[i]:
            i = (i+1)%self.m

        self.hash_map[i] = None

        #rehashing algorithm
        i = (i + 1) % self.m
        while self.hash_map[i]!=None:
            item = self.hash_map[i]
            self.hash_map[i] = None
            self.n -= 1
            self.put(item)
            i = (i + 1) % self.m

        self.n -= 1
        if self.n > 0 and self.n <= self.m//8:
            self.__resize__(self.m//2)

    def __iter__(self):
        list = []
        for item in self.hash_map:
            if item != None:
                list.append(item)
        return iterator(list)

    def __hash_function__(self,key):
        return (hash(key) & 0x7fffffff) % self.m

    def __resize__(self, m):
        tmp_hash_map = probing_hash_map(m) 
        for item in self:
            if item != None:
                tmp_hash_map.put(item)
        self.m = tmp_hash_map.m
        self.n = tmp_hash_map.n
        self.hash_map = tmp_hash_map.hash_map

if __name__ == "__main__":
    hash_map = probing_hash_map(5)
    list = [10,1,3,4,5]

    for i in list:
        hash_map.put(i)

    print("Does map contains 1 = ", hash_map.contains(1))
    print("Does map contains 13 = ", hash_map.contains(13))
    print("Does map contains 7 = ", hash_map.contains(7))
   
    print("Hash map:")
    for k in hash_map:
        print("Key in hash map = ",k)

    print("Deleting 1 from hash map")
    hash_map.delete(1)
    print("Deleting 10 from hash map") 
    hash_map.delete(10)
    print("Deleting 3 from hash map")
    hash_map.delete(3)
    print("Deleting 4 from hash map")
    hash_map.delete(4)

    print("Hash map:")
    for k in hash_map:
        print("Key in hash map = ",k)
