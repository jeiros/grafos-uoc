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
    T = nx.Graph()
    for node in G.nodes():
        T.add_node(node)
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
    print_nodes(G)
    print_Ubitmap(U, G)
    print_etiquetas(etiquetas)

    U.append(v)
    print("chose ", v)
    while len(U) != n:
        print("====")
        print_nodes(G)
        print_Ubitmap(U, G)
        edges_from_node = sorted(G.edges(v, data=True), key=lambda t: t[2].get('weight', 1))
        
        for edge in edges_from_node:
            tgt = edge[1]
            if edge[2]['weight'] < etiquetas[tgt][0] and tgt not in U:
                etiquetas[tgt] = (edge[2]['weight'], v)
        print_etiquetas(etiquetas)
        print("====")
        can_choose = []
        for node in G.nodes():
            if node not in U:
                can_choose.append(node)
        min_aw = Inf
        
        for node in reversed(can_choose):
            if etiquetas[node][0] <= min_aw:
                min_aw = etiquetas[node][0]
                chosen_node = node
        print("chose ", chosen_node)
        T.add_edge(chosen_node, etiquetas[chosen_node][1], weight=G.get_edge_data(etiquetas[chosen_node][1], chosen_node)['weight'])
        U.append(chosen_node)
        v = chosen_node

    print("====")
    print_nodes(G)
    print_Ubitmap(U, G)
    print_etiquetas(etiquetas)
    print("====")
    print("Peso total", T.size(weight="weight"))
    print("Aristas de T", T.edges(data=True))
    return T

def find_root(T):
    return [n for n,d in T.in_degree() if d==0][0]

def preorden(T):
    raiz = find_root(T)
    print(raiz)

    succ = list(T.successors(raiz))
    if len(succ) == 2:
        # Dos hijos
        r1, r2 = succ
    elif len(succ) == 1:
        r1 = succ[0]
        r2 = None
    elif len(succ) == 0:
        # Hoja
        return None


    T_uno = nx.DiGraph()
    T_uno.add_node(r1)
    T_uno.add_edges_from(T.edges(r1))
    for node in nx.descendants(T, r1):
        T_uno.add_edges_from(T.edges(node))
    preorden(T_uno)
    
    if r2 is not None:
        T_dos = nx.DiGraph()
        T_dos.add_node(r2)
        T_dos.add_edges_from(T.edges(r2))
        for node in nx.descendants(T, r2):
            T_dos.add_edges_from(T.edges(node))
        preorden(T_dos)

def inorden(T):
    raiz = find_root(T)

    succ = list(T.successors(raiz))
    if len(succ) == 2:
        # Dos hijos
        r1, r2 = succ
    elif len(succ) == 1:
        r1 = succ[0]
        r2 = None
    elif len(succ) == 0:
        # Hoja
        print(raiz)
        return None

    T_uno = nx.DiGraph()
    T_uno.add_node(r1)
    T_uno.add_edges_from(T.edges(r1))
    for node in nx.descendants(T, r1):
        T_uno.add_edges_from(T.edges(node))
    
    inorden(T_uno)
    print(raiz)

    if r2 is not None:
        T_dos = nx.DiGraph()
        T_dos.add_node(r2)
        T_dos.add_edges_from(T.edges(r2))
        for node in nx.descendants(T, r2):
            T_dos.add_edges_from(T.edges(node))
        inorden(T_dos)

def postorden(T):
    raiz = find_root(T)
    succ = list(T.successors(raiz))
    if len(succ) == 2:
        # Dos hijos
        r1, r2 = succ
    elif len(succ) == 1:
        r1 = succ[0]
        r2 = None
    elif len(succ) == 0:
        # Hoja
        print(raiz)
        return None

    T_uno = nx.DiGraph()
    T_uno.add_node(r1)
    T_uno.add_edges_from(T.edges(r1))
    for node in nx.descendants(T, r1):
        T_uno.add_edges_from(T.edges(node))
    postorden(T_uno)
    
    if r2 is not None:
        T_dos = nx.DiGraph()
        T_dos.add_node(r2)
        T_dos.add_edges_from(T.edges(r2))
        for node in nx.descendants(T, r2):
            T_dos.add_edges_from(T.edges(node))
        postorden(T_dos)
    print(raiz)

def digraph_from_dict_of_lists(adj):
    G = nx.DiGraph()
    for node, neighs in adj.items():
        for n in neighs:
            G.add_edges_from([(node, n)])
    return G

if __name__ == '__main__':
    adjs = {
        1: [2, 5],
        2: [5],
        3: [2, 4, 5],
        4: [5, 6],
    }
    G = nx.from_dict_of_lists(adjs)
    bfs_arbol_generador(G, 1)
    dfs_arbol_generador(nx.petersen_graph(), 0)

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
    kruskal(Gw, minimal=True)
    prim(Gw, 1)


    alt = {
        'A' : {
            'B' : {'weight' : 3},
            'D' : {'weight' : 4},
            'E' : {'weight' : 4},
        },
        'B' : {
            'C' : {'weight' : 10},
            'E' : {'weight' : 2},
            'F' : {'weight' : 3},
        },
        'C' : {
            'F' : {'weight' : 6},
            'G' : {'weight' : 1},
        },
        'D' : {
            'E' : {'weight' : 5},
            'H' : {'weight' : 6},
        },
        'E' : {
            'F' : {'weight' : 11},
            'H' : {'weight' : 2},
            'I' : {'weight' : 1},
        },
        'F' : {
            'G' : {'weight' : 2},
            'I' : {'weight' : 3},
            'J' : {'weight' : 11},
        },
        'G' : {
            'J' : {'weight' : 8},
        },
        'H' : {
            'I' : {'weight' : 4},
        },
        'I' : {
            'J' : {'weight' : 7},
        }
    }
    Galt = nx.from_dict_of_dicts(alt)
    kruskal(Galt)
    prim(Galt, 'A')

    # Tree tests
    tree = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        5: [8, 9],
        7: [10, 11]
    }
    G = digraph_from_dict_of_lists(tree)
    print("PREORDEN")
    preorden(G)
    print("INORDEN")
    inorden(G)
    print("POSTORDEN")
    postorden(G)

    # Ejercicio 28
    letras = {
        'A' : ['B', 'F'],
        'B' : ['C'],
        'C' : ['D', 'G'],
        'D' : ['E']
    }
    G = digraph_from_dict_of_lists(letras)
    print("PREORDEN")
    preorden(G)
    print("INORDEN")
    inorden(G)
    print("POSTORDEN")
    postorden(G)