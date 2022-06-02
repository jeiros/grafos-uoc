import networkx as nx
from distances import print_nodes, print_Ubitmap
import random
from numpy import Inf

def print_etiquetas(dist):
    print("(E(·), ·):|", end="")
    for d in dist.values():
        print(d, "|", end='')
    print("\n")


def dfs_arbol_generador(G, v):
    print("INICIO DETERMINACION DFS RECURSIVO DE UN ARBOL GENERADOR")
    T = nx.Graph()
    for node in G.nodes():
        T.add_node(node)
    estado = {}
    for w in G.nodes():
        estado[w] = 0
    dfsrec(G, v, T, estado)
    return T

def dfsrec(G, v, T, estado):
    estado[v] = 1
    neighbours = sorted(list(G.neighbors(v)))
    for w in neighbours:
        if estado[w] == 0:
            T.add_edge(w, v)
            dfsrec(G, w, T, estado)


def bfs_arbol_generador(G, v):
    print("INICIO DETERMINACION BFS DE UN ARBOL GENERADOR")
    Q = []
    A = []
    T = nx.Graph()
    for node in G.nodes():
        T.add_node(node)
    estado = {}
    for w in G.nodes():
        estado[w] = 0
    estado[v] = 1
    Q.append(v)
    print("===")
    print("Q", Q)
    print("Aristas añadidas -")
    print("A(T)", A)
    while not not Q:
        w = Q[0]
        neighbours = sorted(list(G.neighbors(w)))
        for u in neighbours:
            if estado[u] == 0:
                Q.append(u)
                estado[u] = 1
                T.add_edge(w, u)
                A.append((w, u))
                print("Q", Q)
                print("Aristas añadidas ", (w, u))
                print("A(T)", A)
        Q = Q[1:]
        print("Q", Q)
        print("Aristas añadidas -")
        print("A(T)", A)
        print("===")
    return T

def kruskal(G, minimal=True):
    print("INICIO KRUSKAL")
    T = nx.Graph()
    E = sorted(G.edges(data=True), key=lambda t: t[2].get('weight', 1), reverse=not minimal)

    for edge in E:
        T.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if not nx.is_forest(T):
            print("Arista {}".format(edge))
            T.remove_edge(edge[0], edge[1])
        else:
            print("Arista {} *".format(edge))

    print("Peso total", T.size(weight="weight"))
    return T

def prim(G, v_inicial=None):
    print("BEGIN PRIM")
    n = len(G.nodes)
    if v_inicial is None:
        v = random.choice(list(G.nodes))
    else:
        v = v_inicial
    U = []
    dist = {}
    etiquetas = {}
    E = {}
    for node in G.nodes:
        E[node] = Inf
        etiquetas[node] = (E[node], v)
    
    E[v] = 0
    etiquetas[v] = (0, v)

    print("====")
    print_nodes(G)
    print_Ubitmap(U, G)
    print_etiquetas(etiquetas)
    print("====")


    edges_from_node = sorted(G.edges(v, data=True), key=lambda t: t[2].get('weight', 1))








if __name__ == '__main__':
    adjs = {
        1: [2, 5],
        2: [5],
        3: [2, 4, 5],
        4: [5, 6],
    }
    G = nx.from_dict_of_lists(adjs)
    T = bfs_arbol_generador(G, 1)

    T = dfs_arbol_generador(nx.petersen_graph(), 0)

    w = {
        1 : {
            2 : {'weight': 2},
            3 : {'weight': 4},
            4 : {'weight': 1}
        },
        2 : {
            4 : {'weight': 3},
            5 : {'weight': 10}
        },
        3 : {
            4 : {'weight': 2},
            6 : {'weight': 5}
        },
        4 : {
            5 : {'weight': 2},
            6 : {'weight': 8},
            7 : {'weight': 4}
        },
        5 : {
            7 : {'weight': 6}
        },
        6 : {
            7 : {'weight': 1},
        }
    }
    Gw = nx.from_dict_of_dicts(w)
    T = kruskal(Gw, minimal=True)
    T = prim(G)