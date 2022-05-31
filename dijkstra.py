import networkx as nx
from numpy import Inf

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