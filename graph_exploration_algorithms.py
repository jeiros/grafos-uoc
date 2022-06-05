import networkx as nx

def dfs(G, v):
  print("Inicio DFS")
  P = []
  R = [v]
  estado = {}
  for w in G.nodes:
    estado[w] = 0
  estado[v] = 1
  P.append(v)
  
  print("====")
  print("P", P)
  print("Vértice añadido", v)
  print("Vértice eliminado", "-")
  print("R", R)
  print("====")

  while not not P:
    w = P[-1]
    neighbours = sorted(list(G.neighbors(w)))
    u = neighbours[0]
    for v in neighbours:
      if estado[v] == 0:
        u = v
        break
    if estado[u] == 0:
      P.append(u)
      estado[u] = 1
      R.append(u)
      print("P", P)
      print("Vértice añadido", u)
      print("Vértice eliminado", "-")
    else:
      e = P.pop()
      print("P", P)
      print("Vértice añadido", "-")
      print("Vértice eliminado", e)
    print("R", R)
    print("====")
  print("Fin DFS")
  return R

def dfs_aristas(G, v):
  print("Inicio DFS aristas")
  P = []
  S = []
  estado = {}
  for w in G.nodes:
    estado[w] = 0
  estado[v] = 1
  P.append(v)

  print("====")
  print("P", P)
  print("Arista añadida", "-")
  print("S", S)
  print("====")

  while not not P:
      w = P[-1]
      neighbours = sorted(list(G.neighbors(w)))
      u = neighbours[0]
      for v in neighbours:
        if estado[v] == 0:
          u = v
          break
      if estado[u] == 0:
        P.append(u)
        estado[u] = 1
        S.append([w, u])
        print("P", P)
        print("Arista añadida", [w, u])
      else:
        e = P.pop()
        print("P", P)
        print("Arista añadida", "-")
      print("S", S)
      print("====")
  print("Fin DFS aristas")
  return S

def bfs(G, v):
  print("Inicio BFS")
  Q = []
  R = [v]
  estado = {}
  for w in G.nodes:
    estado[w] = 0
  estado[v] = 1
  Q.append(v)
  
  print("====")
  print("Q", Q)
  print("Vértice añadido", v)
  print("Vértice eliminado", "-")
  print("R", R)
  print("====")

  while not not Q:
    w = Q[0]
    neighbours = sorted(list(G.neighbors(w)))
    for u in neighbours:
      if estado[u] == 0:
        Q.append(u)
        estado[u] = 1
        R.append(u)
        print("Q", Q)
        print("Vértice añadido", u)
        print("Vértice eliminado", "-")
        print("R", R)
    e = Q[0]
    Q = Q[1:]
    print("Q", Q)
    print("Vértice añadido", "-")
    print("Vértice eliminado", e)
    print("R", R)
    print("====")
  print("Fin BFS")
  return R

def bfs_aristas(G, v):
  print("Inicio BFS aristas")
  Q = []
  S = []
  estado = {}
  for w in G.nodes:
    estado[w] = 0
  estado[v] = 1
  Q.append(v)

  print("====")
  print("Q", Q)
  print("Arista añadida", "-")
  print("S", S)
  print("====")

  while not not Q:
      w = Q[0]
      neighbours = sorted(list(G.neighbors(w)))
      for u in neighbours:
        if estado[u] == 0:
          Q.append(u)
          estado[u] = 1
          S.append([w, u])
          print("Q", Q)
          print("Arista añadida", [w, u])
          print("S", S)
      Q = Q[1:]
      print("Q", Q)
      print("Arista añadida", "-")
      print("S", S)
  print("Fin BFS aristas")
  return S

if __name__ == '__main__':
    dod = {
        'A': {
            'B': {"weight": 150},
            'C': {"weight": 320},
            'E': {"weight": 100},
        },
        'B': {
            'C': {"weight": 150},
            'D': {"weight": 175},
        },
        'C': {
            'D': {"weight":  49},
            'E': {"weight": 130},
        },
    }

    adjs = {
        1: [2, 3, 4],
        2: [1, 5],
        3: [1, 6],
        4: [1],
        5: [2, 6],
        6: [3, 5, 7],
        7: [6]
    }

    G = nx.from_dict_of_dicts(dod)
    #dfs(G, "A")
    #bfs(G, "A")
    dfs_aristas(G, "A")
    bfs_aristas(G, "A")


    Galt = nx.from_dict_of_lists(adjs)
    #dfs(Galt, 1)
    #bfs(Galt, 1)
    dfs_aristas(Galt, 1)
    bfs_aristas(Galt, 1)

  # EXAMEN ANTERIOR
    g = {
        'A': ['B', 'D'],
        'B': ['A', 'C', 'D'],
        'C': ['B', 'F', 'E'],
        'D': ['A', 'B'],
        'E': ['C', 'F'],
        'F': ['C', 'E']
    }
    G = nx.from_dict_of_lists(g)
    #bfs(G, 'C')
    #dfs(G, 'C')
    g = {
          'A': {
              'B': {"weight": 5},
              'D': {"weight": 4}
          },
          'B': {
              'C': {"weight": 2},
              'D': {"weight": 10},
          },
          'C': {
              'E': {"weight": 3},
              'F': {"weight": 10}
          },        
          'F': {
              'E': {"weight": 6}
          },
      }
    G = nx.from_dict_of_dicts(g)
    from distances import floyd
    floyd(G)