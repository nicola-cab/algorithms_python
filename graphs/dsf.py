from base.stack import stack

class DSF:
    """ 
        Class that represent a generic interface for deepth search first.
        This class provides also a API to understand if there is a path
        between two different nodes v and w.
        Basically running DFS guarantees to find a path from a source node s 
        to some destination node d. 
        The path could be even the longest or the shortest.. DFS does not check this things

        Complexity:
        O(E) in the worst case
    """

    def __init__(self, g, s):
        self.s = s #source node in graph
        self.edgeTo = [0] * g.get_number_vertices()
        self.marked = [False] * g.get_number_vertices()
        self.dsf(g, s)

    def dsf(self, g, v):
        self.marked[v] = True
        for w in g.get_adj_list(v):
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dsf(g, w)

    def is_path_present(self,v):
        return self.marked[v]

    def get_path_to(self, v):
        if not self.is_path_present(v):
            raise Exception("Path does not exist")
        s = stack()
        while v != self.s:
            s.push(v)
            v = self.edgeTo[v]
        s.push(self.s)
        return s
