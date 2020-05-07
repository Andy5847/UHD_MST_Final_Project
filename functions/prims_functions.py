# -*- coding: utf-8 -*-

def cost(graph, e):
    return graph.edges()[e]['weight']



def is_spanning(graph, subgraph):
    return graph.nodes() == subgraph.nodes()



def possible_prims_edges(G, T):
    possible_e = []
    for e in set(G.edges()) - set(T.edges()):
        for v in T.nodes():
            if v in e:
                possible_e.append(e)
                
    return possible_e



def min_possible_prims_edge(G, T):
    possible_e = possible_prims_edges(G, T)
    min_e = possible_e[0]
    for e in possible_e:
        if cost(G, e) < cost(G, min_e):
            min_e = e
    return min_e

def min_prims_edges(G, T):
    possible_edges = valid_incident_edges(G, T)
    min_cost_edge = possible_edges[0]
    for e in possible_edges:
        if cost(G, e) < cost(G, min_cost_edge):
            min_cost_edge = e
    return min_cost_edge


def valid_incident_edges(G, T):
    
    incident_edges = []
    for e in G.edges():
        for v in T.nodes():
            if v in e:
                incident_edges.append(e)
        

    valid_edges = []
    for e in incident_edges:
        if e[0] not in T.nodes() or e[1] not in T.nodes():
            valid_edges.append(e)
    
    return valid_edges








