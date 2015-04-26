from base.iterator import iterator
from disjoint_set import disjoint_set
from base.pq import min_pq
class MST:

    """ 
    Abstraction for generic spanning tree algorithm
    """
    def __init__(self, weighted_graph, select):
        self.mst = []
        self.weight = 0.0
        if select:
            print("Run kruskal MST")
            self.__kruskal_mst(weighted_graph)
        else: 
            print("Run Prim MST")
            self.__prims_mst(weighted_graph)

    def edges(self):
        return self.mst

    def weight(self):
        return self.weight

    def __kruskal_mst(self, G):
        """
        Kruskal algorithm:
        - Consider edges in ascending order of weight
        - Add next edge to T mst unless this creates a cycle
        Total complexity E*Lg(V)
        """
        djs = disjoint_set([x for x in range(G.V())])
        edges = G.edges()
        edges.sort() # a priority queue would do the same job of sorting
        
        for e in edges:
            v,w,weight = e
            if djs.find(v) != djs.find(w):
                djs.union(v,w)
                self.mst.append(e)
                self.weight += e.weight
        

    def __prims_mst(self, G):
        """ 
            Lazy implementation prim's algorithm.
            Start from vertex s and greedily grow the tree
            Add to T mst the min weight edge with exactly one endpoint in T
            Repeat V-1 times

            This algorithm runs in O(E + V log V) and it is perfect to cope with dense graphs
        """

        marked = [False] * G.V()
        pq = min_pq()
        for e in G.edges():
            pq.insert(e)

        self.__scan(G, 0, marked, pq)

        while not pq.isEmpty():
            e = pq.delElem()
            v,w,weight = e
            if marked[v] and marked[w]:
                continue
            self.mst.append(e)
            self.weight += weight
            if not marked[v]:
                self.__scan(G, v, marked, pq)
            if not marked[w]:
                self.__scan(G, w, marked, pq)

    def __scan(self, G, v, marked, pq):
        if marked[v] == False:
            marked[v] = True
            for e in G.edges_vertex(v):
                pq.insert(e)
