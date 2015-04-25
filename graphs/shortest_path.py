import heapq
from base.iterator import iterator
from base.stack import stack

class shortest_path:

    def __init__(self, G, s):
        """Dijkstra's shortest path algorithm"""
    
        #support lists and pq
        self.__inf = float("inf")
        self.dist = [self.__inf]  * G.V()
        self.path = [None] * G.V()
        self.pq = []
        heapq.heappush(self.pq, (s,0.0))
        self.dist[s] = 0.0

        self.__dijkstra(G,s)

    def get_dist(self, v):
        return self.dist[v]

    def exist_path(self, v):
        return self.__inf != self.dist[v]

    def get_path(self, s):
        e = self.path[s]
        p = stack()
        while e:
            p.push(e)
            e = self.path[e.v]
        return p

    def __dijkstra(self, G, s):
        checked = [s]
        while self.pq:
            elem = heapq.heappop(self.pq)
            self.__relax(G, elem[0], checked) 

    def __relax(self, G, vertex, checked):
        for e in G.edges_vertex(vertex):
            v,w,weight = e
            d = self.dist[v] + weight
            if self.dist[w] > d:
                self.dist[w] = d
                self.path[w] = e
                if w not in checked:
                    checked.append(w)
                    heapq.heappush(self.pq, (w, d))

#def bellman_ford(G):
#    """ Bellman Ford shortest path algorithm to cope to negative edges and loops"""
#    pass
