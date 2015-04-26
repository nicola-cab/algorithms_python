import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) ) 

#graph data structures
from ugraph import undirected_graph
from weight_ugraph import weight_undirect_graph 
from weight_dgraph import weight_direct_graph
from edge import edge

#graph algorithms
from dsf import DSF
from bsf import BSF
from mst import MST
from shortest_path import shortest_path
from max_flow import network_flow

def set_graph(graph):
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)

def set_weight_undirect_graph(graph):
    e1 = edge(0,1,0.1)
    e2 = edge(0,2,0.5)
    e3 = edge(0,3,0.2)
    e4 = edge(1,2,0.1)
    e5 = edge(1,3,1.1)
    e6 = edge(2,3,0.1)
    e7 = edge(2,4,1.5)
    e8 = edge(3,4,0.3) 
    graph.add_edge(e1)
    graph.add_edge(e2)
    graph.add_edge(e3)
    graph.add_edge(e4)
    graph.add_edge(e5)
    graph.add_edge(e6)
    graph.add_edge(e7)
    graph.add_edge(e8)

def set_weight_direct_graph(graph):
    e1 = edge(0,1,0.1)
    e2 = edge(0,2,0.5)
    e3 = edge(0,3,0.2)
    e4 = edge(1,2,0.1)
    e5 = edge(1,3,1.1)
    e6 = edge(2,3,0.1)
    e7 = edge(2,4,1.5)
    e8 = edge(3,4,0.3)
    e9 = edge(4,3,0.2)
    e10 = edge(3,1,10.0)
    e11 = edge(2,1,1.1)
    graph.add_edge(e1)
    graph.add_edge(e2)
    graph.add_edge(e3)
    graph.add_edge(e4)
    graph.add_edge(e5)
    graph.add_edge(e6)
    graph.add_edge(e7)
    graph.add_edge(e8)
    graph.add_edge(e9)
    graph.add_edge(e10)
    graph.add_edge(e11)

def set_negative_weight_direct_graph(graph):
    e1 = edge(0,1,0.1)
    e2 = edge(0,2,0.5)
    e3 = edge(0,3,-0.2)
    e4 = edge(1,2,0.1)
    e5 = edge(1,3,1.1)
    e6 = edge(2,3,0.1)
    e7 = edge(2,4,-1.5)
    e8 = edge(3,4,0.3)
    e9 = edge(4,3,0.2)
    e10 = edge(3,1,10.0)
    e11 = edge(2,1,1.1)
    graph.add_edge(e1)
    graph.add_edge(e2)
    graph.add_edge(e3)
    graph.add_edge(e4)
    graph.add_edge(e5)
    graph.add_edge(e6)
    graph.add_edge(e7)
    graph.add_edge(e8)
    graph.add_edge(e9)
    graph.add_edge(e10)
    graph.add_edge(e11)

def check_graph_properties(graph, vertices):
    print("Number of edges = ", graph.E())
    print("Number of vertices = ", graph.V())
    for v in vertices:
        print("Degree for node ", v, " is ", graph.degree(v))
        print("Check adj list for node ", v)
        for l in graph.edges_vertex(v):
            print(l)
#
# Algorithm for graphs util functions
#
def run_dsf(graph, s, d):
    print("Running DSF algorithm")
    dsf = DSF(graph, s)
    r = dsf.is_path_present(d) 
    print("Exist a path from ",s," to ", d, " == ", r)
    if r == True:
        path = dsf.get_path_to(d)
        print("path:")
        for v in path:
            print( "node: ", v )
        
def run_bsf(graph, s, d):
    print("Running BSF algorithm")
    bsf = BSF(graph, s)
    r = bsf.is_path_present(d) 
    print("Exist a path from ",s," to ", d, " == ", r)
    if r == True:
        print("distance(", s, ",",d,") is ", bsf.get_dist_to(d))
        path = bsf.get_path_to(d)
        print("path:")
        for v in path:
            print( "node: ", v )

def run_mst(G, algo_pick):
    """ 
    Compute MST using a greedy algorithm. 
    Internally MST uses Kruskal algorithm. 
    """
    mst = MST(G, algo_pick) 
    print("Entire graph:")
    for e in G.edges():
        print( e )

    print("MST")
    for e in mst.edges():
        print(e)

if __name__ == "__main__":
    #undirect graph test
    l = [x for x in range(5)]
    graph = undirected_graph(len(l))
    set_graph(graph)
    check_graph_properties(graph, l)

    print("------------------- running dsf --------------------- ")
    run_dsf(graph, 0, 4)
    run_dsf(graph, 1, 2) 
    run_dsf(graph, 4, 3)
    run_dsf(graph, 0, 0)

    print("------------------- running bsf --------------------- ")
    run_bsf(graph, 0, 4)
    run_bsf(graph, 1, 2)
    run_bsf(graph, 4, 3)
    run_bsf(graph, 0, 0)

    print("------------------- running mst --------------------- ")
    w_ugraph = weight_undirect_graph(len(l))
    set_weight_undirect_graph(w_ugraph)
    check_graph_properties(w_ugraph, l)
    print("-------")
    run_mst( w_ugraph, 1 ) #run kruskal
    print("-------") 
    run_mst( w_ugraph, 0)  #run prim

    print("------------------- running shortest path --------------------- ")
    w_dgraph = weight_direct_graph(len(l))
    set_weight_direct_graph(w_dgraph)
    check_graph_properties(w_dgraph, l)
    
    print("Entire graph")
    for e in w_dgraph.edges():
        print(e)

    print("-------")
    print("Dijkstra")
    sp = shortest_path(w_dgraph,0)

    for v in range(w_dgraph.V()):
        if sp.exist_path(v):
            print("Dist path from 0 to ", v, " is =", sp.get_dist(v))
            print("Path is ")
            for e in sp.get_path(v):
                print(e)

    print("-------")
    print("Bellaman Ford")
    set_negative_weight_direct_graph(w_dgraph)
    check_graph_properties(w_dgraph, l)
    
    print("Entire graph")
    for e in w_dgraph.edges():
        print(e)

    sp = shortest_path(w_dgraph,0, 0) #run bellman_ford passing 0 as 3rd argument

    for v in range(w_dgraph.V()):
        if sp.exist_path(v):
            print("Dist path from 0 to ", v, " is =", sp.get_dist(v))
            print("Path is ")
            for e in sp.get_path(v):
                print(e)

    print("------------------- running Max Flow --------------------- ")
    v = [x for x in "sopqrt"]
    g = network_flow(v)
    g.add_edge('s','o',3)
    g.add_edge('s','p',3)
    g.add_edge('o','p',2)
    g.add_edge('o','q',3)
    g.add_edge('p','r',2)
    g.add_edge('r','t',3)
    g.add_edge('q','r',4)
    g.add_edge('q','t',2)
    check_graph_properties(g, v)
    print("Max Flow = ", g.max_flow('s','t'))
