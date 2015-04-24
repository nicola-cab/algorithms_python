from base.queue import queue
from base.stack import stack
class BSF:
    """
        This class exposes a set of APIs to implement a breadth search first.
        Breadth search returns the shortest path for a undirect graph
    """
    def __init__(self, G, s):
        self.s = s
        self.marked = [False]*G.V()
        self.distTo = [-1]*G.V()
        self.edgeTo = [0]*G.V()
        self.bsf(G,s)

    def bsf(self, G, s):
        
        q = queue()
        self.distTo[s] = 0
        self.marked[s] = True
        q.enqueue(s)

        while not q.isEmpty():
            v = q.dequeue()
            for w in G.edges_vertex(v):
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    self.distTo[w] = self.distTo[v] + 1
                    self.marked[w] = True
                    q.enqueue(w)

    def is_path_present(self,v):
        return self.marked[v]

    def get_dist_to(self, v):
        return self.distTo[v]
     
    def get_path_to(self, v):
        if not self.is_path_present(v):
            raise Exception("Path does not exist")
        s = stack()
        while v != self.s:
            s.push(v)
            v = self.edgeTo[v]
        s.push(self.s)
        return s
