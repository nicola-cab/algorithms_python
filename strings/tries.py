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
        def __init__(self, R=128): #by default extended ascii
            self.next = [None]*R #list of children nodes
            self.R = R
            self.val = None

    def __init__(self):
        self.root = self.node()
        self.n = 0
        self.r = self.root.R

    def size(self):
        return self.n

    def is_empty(self):
        return self.size() == 0
    
    def put(self, key, val):
        self.root = self.__put__(self.root, key, val, 0)
    
    def get(self, key):
        node = self.__get__(self.root, key, 0)
        if node == None:   
            raise Exception("String not found")
        return node.val
    
    def delete(self, key):
        self.root = self.__delete__(self.root, key, 0)

    def contains(self, key):
        return self.__get__(self.root, key, 0) != None

    def prefix_strings(self, prefix):
        node = self.__get__(self.root, prefix, 0)
        l_prefix = [ [] for n in node.next if n ]
        i,j = 0,0
        for n in node.next:
            pre = []
            if n:
                pre.append(chr(i)) #append current key 
                pre.extend(self.__trie_nav( node.next[i].next )) #nav tree to find other keys
                l_prefix[j].extend(pre)
                j += 1
            i += 1
        return l_prefix
    
    #
    #   private implementation
    #

    def __put__(self, node, key, val, d):
        if not node:
            node = self.node()
        # insert since end of the string has been reached
        if d == len(key):
            if node.val == None: 
                self.n += 1
            node.val = val
            return node
        
        i = ord(key[d])
        node.next[i] =  self.__put__(node.next[i], key, val, d+1)
        return node
   
    def __get__(self, node, key, d):
        if node == None:
            return None
        if d == len(key):
            return node
        i = ord(key[d])
        return self.__get__(node.next[i], key, d+1)

    def __delete__(self, node, key, d):
        if node == None:
            return None
        if d == len(key):
            if node.val != None:
                self.n -= 1
            node.val = None
        else:
            i = ord(key[d])
            node.next[i] = self.__delete__(node.next[i], key, d+1)

        #delete all subtrie if empty
        if node.val:
            return node
        for i in range(self.r):
            if node.next[i]: return node
        return None

    def __iter__(self):
        return iterator(self.__trie_nav(self.root.next))

    def __trie_nav(self, list):
        q = [list]
        res = [] 
       
        #start a bst 
        while q:
            i = 0
            l = q.pop()
            for e in l:
                if e:
                    res.append(chr(i))
                    q.append(e.next)
                i += 1 
        return res

if __name__ == "__main__":

    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from base.iterator import iterator

    t = trie()
    str = "hello"
    str1 = "world"
    str2 = "can"
    str3 = "I"
    str4 = "enter"
    str_s = [str, str1, str2, str3, str4]

    print("is empty = ", t.is_empty())
    
    #insert strings
    for s in str_s:
        t.put(s, 0)
        print("Processing :", s)

    print("Chars in trie:")
    for c in t:
        print(c)
    
    for s in str_s:
        r = t.contains(s)
        print("contains -->", s," -->", r)
        if t.contains(s) == False:
            raise Exception("Test failed")

    print("Number of keys = ",t.size())
    t.delete("hello")
    print("Number of keys =", t.size())
    try:
        t.get("hello")
    except Exception as e:
        print(e)
        print("Test passed, try to retrieve a key deleted")

    size = t.size()
    t.delete("hello")
    if t.size() == size:
        print("Test passed size is the same after a 'void' deletation")
    else:
        raise Exception("Test failed performing fake deletation")

    t.delete("Hello")
    t.put("Hello", 0)
    print(t.size())
    t.delete("Hello")
    print(t.size())
    
    #test prefix strings
    t.put("Dog", 1)
    t.put("Door",2)
    prefix = t.prefix_strings("Do")
    for p in prefix:
        print("Base: Do -- Prefix: ",p, " = ", "Do" + ''.join(p))
        
    
