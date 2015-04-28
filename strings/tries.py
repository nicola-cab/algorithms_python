class trie:
    """
        Trie implementation. 
        Complexity analysis:
        - search hint: L
        - search miss: LOGr(N) where r is the number of symbols
        - insert: L
        - space: O(R + 1)N == a lot of space is wasted
    """
    
    class node:
        def __init__(self):
            self.next = {} #list of children nodes

    def __init__(self):
        self.root = self.node() 
    
    def put(self, key, val):
        self.root = self.__put__(self.root, key, val, 0)
    
    def get(self, key, val):
        node = self.__get__(self.root, key, 0)
        if node == None:   
            raise Exception("String not found")
        return node.val
    
    def contains(self, key):
        return self.__get__(key) != None
    
    def __put__(self, node, key, val, d):
        if not node:
            node = self.node()
        # insert since end of the string has been reached
        if d == len(key):
            node.val = val
            return node
        
        i = key[d]
        node.next[i] = self.put(node.next[i], key, val, d+1)
        return node
   
    def __get__(self, node, key, val, d):
        if node == None:
            return None
        if d == len(key):
            return node
        i = key[d]
        return self.__get__(node.next[i], key, d+1)
        

if __name__ == "__main__":
    t = trie()
    str = "hello"
    str1 = "world"
    str2 = "can"
    str3 = "I"
    str4 = "enter"
    str_s = [str, str1, str2, str3, str4]
    
    #insert strings
    for s in str_s:
        print("Processing :", s)
        for c in s:
            t.put(c, 0)
    