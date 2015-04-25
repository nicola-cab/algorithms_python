import heapq
from base.iterator import iterator
from base.stack import stack

class shortest_path:

    def __init__(self, G, s, choice = 1): 
        """
            Shortest path algorithm:
            - 1 to execute Dijkstra
            - 2 to execute Bellman Ford
        """
    
        #support lists and pq
        self.__inf = float("inf")
        self.dist = [self.__inf]  * G.V()
        self.path = [None] * G.V()
        self.pq = []
        heapq.heappush(self.pq, (s,0.0))
        self.dist[s] = 0.0

        if choice == 1: 
            self.__dijkstra(G,s)
        elif choice == 0:
            self.__bellman_ford(G,s)
        else:
            raise Exception("Error selecting algorighm 1) Dijkstra 2) Bellman Ford")

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
        """
        Complexity is O(E Log V).
        I am using an extra array to store verteces already visited.
        Then I am wasting O(V) space. Using a Indexed PQ should solve this problem
        Using a Fibonacci tree will improve time complexity.
        """
        checked = [s]
        while self.pq:
            elem = heapq.heappop(self.pq)
            self.__relax(G, elem[0], checked) 

    def __relax(self, G, vertex, checked):
        for e in G.edges_vertex(vertex):
            v,u,w = e
            d = self.dist[v] + w
            if self.dist[u] > d:
                self.dist[u] = d
                self.path[u] = e
                if w not in checked:
                    checked.append(u)
                    heapq.heappush(self.pq, (u, d))

    def __bellman_ford(self, G, s):
        """
        bellman ford algorithm allows processing of graphs with negative weight edges
        Algorithm uses relax as such as Dijkstra. it applies relexation V-1 times.
        Algorithm complexity is O(EV). 

        """
        for v in range(G.V()):
            for e in G.edges_vertex(v):
                v,u,w = e
                d = self.dist[v] + w
                if self.dist[u] > d:
                    self.dist[u] = d
                    self.path[u] = e

        #check for cycle.
        for e in G.edges():
            v,u,w = e
            if self.dist[v] + w < self.dist[u]:
                raise Exception("Graph contains negative cycle")
