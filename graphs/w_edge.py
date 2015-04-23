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

    def either(self):
        return self.v

    def other(self, v):
        if v == self.v: 
            return self.w
        return self.v

    def edge_cmp(self, other):
        return cmp(self.weight, other.weight)
