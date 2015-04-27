#reusing edge data strucutre using weigth as capacity
from edge import edge 
from base.iterator import iterator

class network_flow:
    """
    Network flow representation
    """
    def __init__(self,  V):
        self.flow = {}
        self.adj_list = {}
        self.v = len(V)
        self.e = 0
        for v in V:
            self.adj_list[v] = []

    def V(self):
        return self.v

    def E(self):
        return self.e
    
    def degree(self, v):
        return len(self.adj_list[v])

    def edges_vertex(self,v):
        return iterator(self.adj_list[v])
    
    def get_edges(self):
        l = []
        for v in range(self.v):
            for e in self.adj_list[v]:
                l.append(e)
        return l

    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")

        self.e += 1

        #define two edges u->v and v->u 
        e  = edge(u,v,w)
        re = edge(v,u,0)
        #adding reverse edge
        e.re = re
        re.re = e
        #add edges
        self.adj_list[u].append(e)
        self.adj_list[v].append(re)
        #setting default flows
        self.flow[e]=0
        self.flow[re]=0

    #
    # max flow implementation
    #
    def max_flow(self, source, sink):
        """ Max flow implementation """
        path = self.__find_path(source, sink, [])
        while path != None:
            #compute flow left for edges
            flows = [e.weight - self.flow[e] for e in path]

            #pick min flow
            f = min(flows)

            #add flow in e and remove flow from re
            for e in path:
                self.flow[e] += f
                self.flow[e.re] -= f
            path = self.__find_path(source, sink, [])

        #sum min flow
        return sum(self.flow[e] for e in self.edges_vertex(source) )

    def __find_path(self, source, sink, path):
        """ 
        Find path: basically as long as there is path from source to sink with available 
        capacity in all edges in the path we send flow along these paths. 
        """
        if source == sink:
            return path

        for e in self.edges_vertex(source):
            edge_source, edge_sink, edge_capacity = e
            flow = edge_capacity - self.flow[e]
            if flow > 0 and e not in path:
                result = self.__find_path(edge_sink, sink, path + [e])
                if result:
                    return result 
