from base.iterator import iterator
class w_edge:
    """
        Genearal abstraction for a weighted edge.
    """
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        return "(" + str(self.v) + " - " + str(self.w) + ")" + " weight = " + str(self.weight)
   
    def __iter__(self):  #compatible with python 3.x
        return iterator([self.v, self.w, self.weight])
         
    def __lt__(self, other):  #compatible only with python 3.x
        return self.weight < other.weight

    def __cmp__(self, other): #compatible with python 2.x
        return cmp(self,other)