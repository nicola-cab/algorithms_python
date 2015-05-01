class tst:
    """
        Ternary search tree.
        Creating a data structure that contains the keys and  the values inside the node itself.
        All the keys are divided into:
            - left node-tst all the keys less than current key
            - center node-tst all the keys equal than current key
            - right node-tst all the keys greater than current key
    """

    class node:
        def __init__(self):
            self.key = 0
            self.val = None
            self.left, self.mid, self.right = None, None, None

    def __init__(self):
        self.n = 0
        self.root = None
    
    def size(self):
        return self.n
    
    def is_empty(self):
        return self.size() == 0

    def put(self, key, value):
        self.root = self.__put__(self.root, key, value, 0)
        self.n += 1 
    
    def get(self, key):
        node = self.__get__(self.root, key, 0)
        if not node:
            raise Exception("Key not found")
        return node.val
    
    def contains(self, key):
        return self.__get__(self.root, key, 0) != None
        
    def prefix_match(self, prefix):
        """
            return all the keys with a given prefix
        """
        node = self.__get__(self.root, prefix, 0)
        if node == None:
            raise Exception("Prefix not found")
        if node.val != None:
            return [prefix]
        else:
            list = []
            self.__tst_nav(node.mid, prefix, list)
            return list
    
    def wildcard_match(self, wildcard):
        """
            keys that match wildcard passed. eg: .he --> she and the
        """
        pass
    
    def longest_prefix(self, query):
        """
            string that is the longest prefix. eg sheel --> sheels 
        """
        if query == None or len(query) == 0:
            return None
        
        node = self.root
        length = 0
        i = 0
        while node != None and i < len(query):
            c = query[i]
            if   c < node.key: node = node.left
            elif c > node.key: node = node.right
            else:
                i += 1
                if node.val != None: 
                    length = i
                node = node.mid
        return query[:length]        
   
    def __tst_nav(self, node, prefix, list):
        """
            recursively traverse the tst and grab as much keys as possible in order to 
            find all the prefix strings
        """
        if node == None:
            return
        
        self.__tst_nav(node.left, prefix, list)
        if node != None:
            prefix += node.key
            list.append( prefix )
        self.__tst_nav(node.mid, prefix, list)
        prefix = prefix[:-1]
        self.__tst_nav(node.right, prefix, list)
       

    def __put__(self, node, key, value, d):
        c = key[d]
        if node == None:
            node = self.node()
            node.key = c
        if c < node.key:
            node.left = self.__put__(node.left, key, value, d)
        elif c > node.key:
            node.right = self.__put__(node.right, key, value, d)
        elif (d < len(key)-1):
            node.mid = self.__put__(node.mid, key, value, d+1)
        else:
            node.val = value
        return node
    
    def __get__(self, node, key, d):
        if node == None:
            return None
        c = key[d]
        if c < node.key:
            return self.__get__(node.left, key, d)
        elif c > node.key:
            return self.__get__(node.right, key, d)
        elif d < len(key)-1:
            return self.__get__(node.mid, key, d+1)
        else:
            return node
        
if __name__ == "__main__":
    str  = "hello"
    str1 = "world"
    str2 = "Can"
    str3 = "I"
    str4 = "speak"
    str5 = "with"
    str6 = "you"
    str7 = "sponge"
    str8 = "spongebob"

    t = tst()
    strs = [str, str1, str2, str3, str4, str5, str6, str7, str8]
    for s in strs:
        print("Putting: ", s)
        t.put(s, 10)
        
    for s in strs:
        print("Searching for :", s)
        print(t.contains(s))
        
    l = t.prefix_match("sp")
    print("List of keys that start with sp")
    print(l)
    
    long = t.longest_prefix("sponge")
    print("Longest prefix = ", long)
    long = t.longest_prefix("spongebob4")
    print("Longest prefix = ", long)
    