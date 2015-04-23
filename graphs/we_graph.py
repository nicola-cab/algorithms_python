from base.iterator import iterator
class we_graph:
    """
        Abstraction for a weighted edge graph
    """

    def __init__(self, v):
        self.v = v
        self.e = 0
        self.adj_list = [None] * v
        for i in range(v):
            self.adj_list[i] = []

    def get_number_vertices(self):
        return self.v

    def get_number_edges(self):
        return self.e

    def get_degree(self, v):
        return len(self.adj_list[v])

    def add_edge(self, e):
        v = e.either()
        w = e.other(v)
        self.adj_list[v].append(e)
        self.adj_list[w].append(e)
        self.e += 1

    def get_adj_list(self, v):
        return iterator(self.adj_list[v])
