import networkx as nx
from numpy import Inf
import numpy as np
from collections import OrderedDict

def print_nodes(G):
    print("Vértices:|", end="")
    for n in G.nodes():
        print(n, "|", end='')
    print("\n")

def print_Ubitmap(U, G):
    print("U:|", end="")
    for n in G.nodes():
        if n in U:
            print(1, "|", end='')
        else:
            print(0, "|", end='')
    print("\n")

def print_etiquetas(dist):
    print("(dist(·), ·):|", end="")
    for d in dist.values():
        print(d, "|", end='')
    print("\n")
    
def dijkstra(G, s):
    print("BEGIN DIJKSTRA")
    U = set()
    dist = {}
    etiquetas = {}
    
    for v in G.nodes:
        dist[v] = Inf
        etiquetas[v] = (dist[v], s)

    dist[s] = 0
    etiquetas[s] = (dist[s], s)
    print("====")
    print_nodes(G)
    print_Ubitmap(U, G)
    print_etiquetas(etiquetas)
    print("====")
    
    while len(U) != len(G.nodes):
        can_choose = []
        for node in G.nodes():
            if node not in U:
                can_choose.append(node)
        current_node_weight = Inf
        for node in can_choose:
            if dist[node] < current_node_weight:
                current_node_weight = dist[node]
                next_node = node

        print("next_node", next_node)
        U.add(next_node)
        print_nodes(G)
        print_Ubitmap(U, G)
        for v in sorted(list(G.neighbors(next_node))):
            if (dist[next_node] + G.get_edge_data(next_node, v)['weight']) < dist[v]:
                dist[v] = dist[next_node] + G.get_edge_data(next_node, v)['weight']
                etiquetas[v] = (dist[v], next_node)
        print_etiquetas(etiquetas)
        print("====")
    return dist

def distancias_no_ponderado(G, s):
    print("BEGIN DISTANCIAS NO PONDERADO")
    Q = []
    estado={}
    dist={}

    for w in G.nodes():
        estado[w] = 0
        dist[w] = Inf
    
    estado[s] = 1
    dist[s] = 0
    Q.append(s)

    print("====")
    print("Q", Q)
    print("Vértice añadido", s)
    print("Vértice eliminado", "-")
    print("dist", list(dist.values()))
    print("====")
    while not not Q:
        w = Q[0]
        neighbours = sorted(list(G.neighbors(w)))
        for u in neighbours:
            if estado[u] == 0:
                Q.append(u)
                estado[u] = 1
                dist[u] = dist[w] + 1
                print("Q", Q)
                print("Vértice añadido", u)
                print("Vértice eliminado", "-")
                print("dist", list(dist.values()))
        e = Q[0]
        Q = Q[1:]
        print("Q", Q)
        print("Vértice añadido", "-")
        print("Vértice eliminado", e)
        print("dist", list(dist.values()))
    return dist

def floyd(G):
    print("BEGIN FLOYD")
    n = len(G.nodes())
    A = list(G.edges())
    d = []
    x = np.empty(shape=(n, n))
    for _ in range(n):
        d.append(
            np.full_like(x, fill_value=Inf)
        )


    for i in range(n):
        for j in range(n):
            if i==j:                
                d[0][i, j] = 0
            elif ((list(G.nodes())[i], list(G.nodes())[j]) in A) or (list(G.nodes())[j], list(G.nodes())[i]) in A   :
                d[0][i, j] = G.get_edge_data(list(G.nodes())[i], list(G.nodes())[j])["weight"]
            else:
                d[0][i, j] = Inf
    print(G.nodes())
    print(d[0])

    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                d[k][i, j] = min(
                    d[k-1][i, j],
                    d[k-1][i, k] + d[k-1][k , j]
                )
    for di in d:
        print("===")
        print(di)
    return d[-1]

if __name__ == '__main__':
    adjs = {
        'V': {
            'M': {"weight": 6},
            'CS': {"weight": 5},
            'SM': {"weight": 2},
        },
        'M': {
            'T': {"weight": 7},
            'CS': {"weight": 3},
        },
        'CS': {
            'PV': {"weight": 4},
        },
        'SM' : {
            'F': {"weight": 1},
        },
        'F' : {
            'PV': {"weight": 4},
            'VS': {"weight":4},
        },
        'VS' : {
            'SR' : {"weight": 2},
        },
        'SR' : {
            'PV': {"weight": 4},
            'T': {"weight": 3},
        }
    }

    adjtwo = {
        1 : {
            2: {'weight' : 2},
            3: {'weight' : 4},
            4: {'weight' : 1},
        },
        2:{
            4: {'weight':3},
            5: {'weight':10},
        },
        3:{
            4: {'weight':2},
            6:{'weight':5},
        },
        4:{
            5: {'weight':2},
            6:{'weight':8},
            7:{'weight':4},
        },
        5:{
            7:{'weight':6},
        },
        6:{
            7:{'weight':1}
        }
    }


    G = nx.from_dict_of_dicts(adjtwo)
    dijkstra(G, 1)

    adjs = {
        1: [2, 3, 4],
        2: [1, 5],
        3: [1, 6],
        4: [1],
        5: [2, 6],
        6: [3, 5, 7],
        7: [6]
    }
    Galt = nx.from_dict_of_lists(adjs)
    distancias_no_ponderado(Galt, 1)


    ciudades = {
        'Lleida' : {
            'Manresa' : {'weight' : 118},
            'Tarragona' : {'weight' : 91},
        },
        'Tarragona' : {
            'Barcelona' : {'weight' : 105},
        },
        'Manresa' : {
            'Girona' : {'weight' : 157},
            'Barcelona' : {'weight' : 56},
        },
        'Barcelona' : {
            'Girona' : {'weight' : 96},
        },
    }

    Gc = nx.from_dict_of_dicts(ciudades)
    floyd(Gc)