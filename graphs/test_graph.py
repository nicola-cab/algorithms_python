import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) ) 

from ugraph import undirected_graph
from we_graph import we_graph
from w_edge import w_edge
from dsf import DSF
from bsf import BSF
from mst import mst

def set_graph(graph):
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 2)
    graph.add_edge(4, 3)

def set_weight_graph(graph):
    e1 = w_edge(0,1,0.1)
    e2 = w_edge(0,2,0.5)
    e3 = w_edge(0,3,0.2)
    e4 = w_edge(1,2,0.1)
    e5 = w_edge(1,3,1.1)
    e6 = w_edge(2,3,0.1)
    e7 = w_edge(2,4,1.5)
    e8 = w_edge(3,2,2.1)
    e9 = w_edge(3,4,0.3) 
    e10 = w_edge(4,3,0.2)
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

def check_graph_properties(graph):
    print("Number of edges = ", graph.get_number_edges())
    print("Number of vertices = ", graph.get_number_vertices())
    print("Degree for node 0 = ", graph.get_degree(0))
    print("Degree for node 1 = ", graph.get_degree(1))
    print("Degree for node 2 = ", graph.get_degree(2))
    print("Degree for node 3 = ", graph.get_degree(3))
    print("Degree for node 4 = ", graph.get_degree(4))

    print("Check adj list for node 0")
    for v in graph.get_adj_list(0):
        print(v)
    print("Check adj list for node 1")
    for v in graph.get_adj_list(1):
        print(v)

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
    

if __name__ == "__main__":
    #undirect graph test
    graph = undirected_graph(5)
    set_graph(graph)
    check_graph_properties(graph)
    #run dsf
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
    we_graph = we_graph(5)
    set_weight_graph(we_graph)
    check_graph_properties(we_graph) 

