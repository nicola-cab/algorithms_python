from base.iterator import iterator
from base.pq import min_pq

class mst:
    """ 
    Abstraction for generic spanning tree algorithm
    """

    def __init__(self, weighted_graph):
        self.MST = []

    def edges(self):
        return self.MST

    def weight(self):
        pass

    def __kruskal_mst(self, G):
        """
        Kruskal algorithm:
        - Consider edges in ascending order of weight
        - Add next edge to T mst unless this creates a cycle

        this algorithms use a priority queue. Building it costs O(E)
        Total complexity E*Lg(V)
        """

        pq = min_pq()
        for e in G.get_adj_list():
            pq.insert(e)

        







