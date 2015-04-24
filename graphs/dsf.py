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

    def __init__(self, G, s):
        self.s = s #source node in graph
        self.edgeTo = [0] * G.V()
        self.marked = [False] * G.V()
        self.dsf(G, s)

    def dsf(self, G, v):
        self.marked[v] = True
        for w in G.edges_vertex(v):
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dsf(G, w)

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
