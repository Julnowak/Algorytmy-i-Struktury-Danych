# Skończone
import graf_mst
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

    def __str__(self):
        return self.key


class Edge:
    def __init__(self, vertex1, vertex2, weight=1):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def __str__(self):
        return f'({self.vertex1}->{self.vertex2}, {self.weight})'


class AdjacencyList:
    def __init__(self):
        self.mapa = dict()  # Konwertuje węzeł na jego indeks
        self.lista = []  # Lista z węzłami
        self.adjlist = dict()  # Z indeksami do elementów
        self.edges = dict() # List z krawędziami
        self.get_weight = dict()  # Konwertuje indeksy na krawędź

    def insertVertex(self, vertex):
        if vertex in self.lista:
            raise Exception('Węzeł już istnieje')
        self.lista.append(vertex)
        idx = self.lista.index(vertex)
        self.mapa[vertex] = idx
        self.adjlist[idx] = []

    def insertEdge(self, vertex1, vertex2, weight=1):
        if vertex1 in self.lista and vertex2 in self.lista and vertex1 != vertex2:
            v1 = self.getVertexIdx(vertex1)
            v2 = self.getVertexIdx(vertex2)
            if v1 not in self.adjlist[v2] or v2 not in self.adjlist[v1]:
                self.adjlist[v1].append(v2)
                self.adjlist[v1].sort()

                self.adjlist[v2].append(v1)
                self.adjlist[v2].sort()
            self.edges[self.getVertexIdx(vertex1), self.getVertexIdx(vertex2)] = Edge(vertex1, vertex2, weight)
            self.get_weight[(v1, v2)] = weight
        else:
            raise Exception('Nie ma takiego wierzchołka')

    def deleteVertex(self, vertex):
        if vertex in self.lista:
            v = self.getVertexIdx(vertex)
            print(v)
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
            newl.append((p, self.get_weight[(vertex_idx, p)]))
        return newl

    def size(self):
        return len(self.list_of_edges())

    def list_of_edges(self):
        lista = []
        for k, v in self.edges.items():
            lista.append((k[0], k[1], v.weight))
        return lista

    def order(self):
        return len(self.adjlist)


class UnionFind:
    def __init__(self, n):
        self.n = n  # ROZMIAR STRUKTURY
        self.p = list(range(n))
        self.size = [0] * n   # WIELKOŚĆ

    def find(self, v):
        return self._find(self.p[v], v)

    def _find(self, root, v):
        if root == v:
            pass
        else:
            v = root
            root = self.p[v]
            self._find(root, v)
        return root

    def union_sets(self, s1, s2):
        r1 = self.find(s1)
        r2 = self.find(s2)

        if self.same_component(r1, r2):
            pass    # W tym samym podzbiorze
        else:
            sz1 = self.size[r1]
            sz2 = self.size[r2]
            if sz1 < sz2:   # Mniejsze pod większe
                self.p[r1] = r2
                self.size[r1] += 1
                if sz1 > sz2:
                    self.size[r2] = sz1
                else:
                    self.size[r2] = sz2

            elif sz1 >= sz2:
                self.p[r2] = r1
                if sz1 > sz2:
                    self.size[r2] = sz1
                else:
                    self.size[r2] = sz2
                    if sz1 > sz2:
                        self.size[r1] = sz1
                    else:
                        self.size[r1] = sz2

    def same_component(self, s1, s2):
        return self.find(s1) == self.find(s2)


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")


def Kruskal(G):
    l = []
    Q = sorted(G.list_of_edges(), reverse=False, key=lambda x: x[2])
    Uf = UnionFind(G.order())
    for tup in Q:
        if not Uf.same_component(tup[0], tup[1]):
            l.append((Gr.getVertex(tup[0]).key, Gr.getVertex(tup[1]).key, tup[2]))
            Uf.union_sets(tup[0], tup[1])

    Y = AdjacencyList()
    for i in sorted(l, key=lambda x: x[1]):

        if Vertex(i[0]) not in Y.mapa.keys():
            Y.insertVertex(Vertex(i[0]))
        if Vertex(i[1]) not in Y.mapa.keys():
            Y.insertVertex(Vertex(i[1]))
        Y.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])
        Y.insertEdge(Vertex(i[1]), Vertex(i[0]), i[2])

    return Y

if __name__ == '__main__':

    Gr = AdjacencyList()

    for i in graf_mst.graf:
        if Vertex(i[0]) not in Gr.mapa.keys():
            Gr.insertVertex(Vertex(i[0]))
        if Vertex(i[1]) not in Gr.mapa.keys():
            Gr.insertVertex(Vertex(i[1]))
        Gr.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])
        Gr.insertEdge(Vertex(i[1]), Vertex(i[0]), i[2])

    new = Kruskal(Gr)
    printGraph(new) # Otrzymana lista krawędzi jest identyczna,jak w zadaniu z MST
