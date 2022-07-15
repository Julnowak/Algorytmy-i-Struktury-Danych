# Skończone
from math import inf

class Vertex:
    def __init__(self, key, colour=None):
        self.key = key
        self.colour = colour

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    def __repr__(self):
        return f'{self.key}'


class Edge:
    def __init__(self, vertex1, vertex2, capacity=1, isResidual=False):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.capacity = capacity    # Pojemność
        self.flow = 0              # początkowy przepływ
        self.residual = capacity    # początkowy przepływ resztowy
        self.isResidual = isResidual    #  czy krawędź jest resztowa

    def __repr__(self):
        return f'{self.capacity} {self.flow} {self.residual} {self.isResidual}'


class AdjacencyList:
    def __init__(self):
        self.mapa = dict()  # Konwertuje węzeł na jego indeks
        self.lista = []  # Lista z węzłami
        self.adjlist = dict()  # Z indeksami do elementów
        self.edges = dict()   # List z krawędziami
        self.get_capacity = dict()  # Konwertuje indeksy na wagi
        self.get_resid = dict()

    def insertVertex(self, vertex):
        if vertex in self.lista:
            raise Exception('Węzeł już istnieje')
        self.lista.append(vertex)
        idx = self.lista.index(vertex)
        self.mapa[vertex] = idx
        self.adjlist[idx] = []

    def insertEdge(self, vertex1, vertex2, capacity=1, isResidual=False):
        if vertex1 in self.lista and vertex2 in self.lista and vertex1 != vertex2:
            v1 = self.getVertexIdx(vertex1)
            v2 = self.getVertexIdx(vertex2)
            if v1 not in self.adjlist[v2] or v2 not in self.adjlist[v1]:
                self.adjlist[v1].append(v2)
                self.adjlist[v1].sort()

                self.adjlist[v2].append(v1)
                self.adjlist[v2].sort()

            self.edges[self.getVertexIdx(vertex1), self.getVertexIdx(vertex2)] = Edge(vertex1, vertex2, capacity, isResidual)
            self.get_capacity[(v1, v2)] = capacity
            self.get_resid[(v1, v2)] = isResidual
        else:
            raise Exception('Nie ma takiego wierzchołka')

    def deleteVertex(self, vertex):
        if vertex in self.lista:
            v = self.getVertexIdx(vertex)
            lista = [x for x in self.adjlist[v]]

            for y in lista:
                self.deleteEdge(vertex, self.getVertex(y))

            self.adjlist.pop(v)
            self.mapa.pop(vertex)
            self.lista.remove(vertex)

            for x in self.lista:
                self.mapa[x] = self.lista.index(x)

            old = self.adjlist.copy()
            for k, j in old.items():
                for q in j:
                    if q > v:
                        idx = j.index(q)
                        j[idx] = q - 1
                if k > v:
                    self.adjlist[k - 1] = j
                    self.adjlist.pop(k)
                else:
                    self.adjlist[k] = j

        else:
            raise Exception('Nie ma takiego wierzchołka')

    def deleteEdge(self, vertex1, vertex2):
        if vertex1 in self.lista and vertex2 in self.lista:
            v1 = self.getVertexIdx(vertex1)
            v2 = self.getVertexIdx(vertex2)

            self.adjlist[v1].remove(v2)
            self.adjlist[v2].remove(v1)
        else:
            raise Exception('Nie ma takiego wierzchołka')

    def getVertexIdx(self, vertex):
        return self.mapa[vertex]

    def getVertex(self, vertex_idx):
        return self.lista[vertex_idx]

    def neighbours(self, vertex_idx):
        lista = self.adjlist[vertex_idx]
        newl = []
        for p in lista:
            newl.append((p, self.get_capacity[(vertex_idx, p)], self.edges[(vertex_idx, p)].residual))
        return newl

    def size(self):
        return len(self.list_of_edges())

    def list_of_edges(self):
        lista = []
        for k, v in self.adjlist.items():
            for i in v:
                lista.append((self.getVertex(k).key, self.getVertex(i).key))
        return lista

    def order(self):
        return len(self.adjlist)


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for (j, w, r) in nbrs:
            print(g.edges[(i, j)], end=";")
        print()
    print("-------------------")


def BFS(g, s=0):
    visited = [False] * len(g.adjlist.keys())
    parent = [None] * len(g.adjlist.keys())

    Q = [s]
    visited[s] = True

    while Q:
        el = Q.pop(0)
        for v in g.neighbours(el):
            if visited[v[0]] is False and v[2] > 0:
                Q.append(v[0])
                visited[v[0]] = True
                parent[v[0]] = el
    return parent


def MinCapacity(g, start, end, parlist):
    cur = end
    mincap = inf

    if parlist[end] is not None:
        while cur != start:
            res = g.edges[(parlist[cur], cur)].residual
            if res < mincap:
                mincap = res
            cur = parlist[cur]
        return mincap
    else:
        return 0


def Aug_path(g, start, end, parlist, mincap):
    cur = end

    if parlist[end] is not None:
        while cur != start:

            # rzeczywista
            g.edges[(parlist[cur], cur)].flow += mincap
            g.edges[(parlist[cur], cur)].residual -= mincap

            # resztowa
            g.edges[(cur, parlist[cur])].residual += mincap
            cur = parlist[cur]
    else:
        return 0


def Ford_Fulkerson(g, source, sink):
    p = BFS(g,source)
    w = MinCapacity(g, source, sink, p)
    suma = w
    while w > 0:

        Aug_path(g, source, sink, p, w)
        p = BFS(g)

        w = MinCapacity(g, source, sink, p)
        suma += w

    return suma


if __name__ == '__main__':

    # Test nr 1  ----> Odp. 3
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
    G = AdjacencyList()

    for i in graf_0:
        if Vertex(i[0]) not in G.mapa.keys():
            G.insertVertex(Vertex(i[0]))
        if Vertex(i[1]) not in G.mapa.keys():
            G.insertVertex(Vertex(i[1]))
        G.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])

    for i in graf_0:
        if (G.getVertexIdx(Vertex(i[1])), G.getVertexIdx(Vertex(i[0]))) not in G.edges.keys():
            G.insertEdge(Vertex(i[1]), Vertex(i[0]), 0, True)

    suma = Ford_Fulkerson(G, G.mapa[Vertex('s')], G.mapa[Vertex('t')])
    print(suma)
    printGraph(G)

    # Test nr 2  ----> Odp. 23
    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9),
              ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    G = AdjacencyList()

    for i in graf_1:
        if Vertex(i[0]) not in G.mapa.keys():
            G.insertVertex(Vertex(i[0]))
        if Vertex(i[1]) not in G.mapa.keys():
            G.insertVertex(Vertex(i[1]))
        G.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2], False)

    for i in graf_1:
        if (G.getVertexIdx(Vertex(i[1])), G.getVertexIdx(Vertex(i[0]))) not in G.edges.keys():
            G.insertEdge(Vertex(i[1]), Vertex(i[0]), 0, True)

    suma = Ford_Fulkerson(G, G.mapa[Vertex('s')], G.mapa[Vertex('t')])
    print(suma)
    printGraph(G)

    # # Test nr 3  ----> Odp. 5
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
           ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    G = AdjacencyList()

    for i in graf_2:
        if Vertex(i[0]) not in G.mapa.keys():
            G.insertVertex(Vertex(i[0]))
        if Vertex(i[1]) not in G.mapa.keys():
            G.insertVertex(Vertex(i[1]))
        G.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])

    for i in graf_2:
        if (G.getVertexIdx(Vertex(i[1])), G.getVertexIdx(Vertex(i[0]))) not in G.edges.keys():
            G.insertEdge(Vertex(i[1]), Vertex(i[0]), 0, True)

    suma = Ford_Fulkerson(G, G.mapa[Vertex('s')], G.mapa[Vertex('t')])
    print(suma)
    printGraph(G)

    # # Test nr 3  ----> Odp. 6
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5),
              ('d', 'b', 7), ('d', 'c', 4)]
    G = AdjacencyList()

    for i in graf_3:
        if Vertex(i[0]) not in G.mapa.keys():
            G.insertVertex(Vertex(i[0]))
        if Vertex(i[1]) not in G.mapa.keys():
            G.insertVertex(Vertex(i[1]))
        G.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])

    for i in graf_3:
        if (G.getVertexIdx(Vertex(i[1])), G.getVertexIdx(Vertex(i[0]))) not in G.edges.keys():
            G.insertEdge(Vertex(i[1]), Vertex(i[0]), 0, True)

    suma = Ford_Fulkerson(G, G.mapa[Vertex('s')], G.mapa[Vertex('t')])
    print(suma)
    printGraph(G)
