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
            self.val = 0
            self.left, self.mid, self.right = None, None, None

    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.__put__(self.root, key, value, 0)

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

if __name__ == "__main__":
    str = "hello"
    str1 = "world"
    str2 = "Can"
    str3 = "I"
    str4 = "speak"
    str5 = "with"
    str6 = "you"

    t = tst()
    strs = [str, str1, str2, str3, str4, str5, str6]
    for s in strs:
        print("Processing: ", s)
        t.put(s, 10)
