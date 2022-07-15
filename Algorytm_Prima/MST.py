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
        self.edges = []  # List z krawędziami
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
            self.edges.append(Edge(vertex1, vertex2, weight))
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

    # Trzeba zmienić neighbours, bo przyjmuje krotkę indeks waga
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
        for k, v in self.adjlist.items():
            for _ in v:
                lista.append((self.getVertex(k).key, self.getVertex(i).key))
        return lista

    def order(self):
        return len(self.adjlist)


def MST(G):
    length = 0
    intree = [0] * G.order()
    distance = [inf] * G.order()
    parent = [-1] * G.order()

    # Szkielet MST
    newG = AdjacencyList()

    for ve in graf_mst.graf:
        if Vertex(ve[0]) not in newG.mapa.keys():
            newG.insertVertex(Vertex(ve[0]))
        if Vertex(ve[1]) not in newG.mapa.keys():
            newG.insertVertex(Vertex(ve[1]))

    v = 0
    distance[v] = 0
    while intree[v] == 0:
        intree[v] = 1
        length += distance[v]
        for ver in G.neighbours(v):
            if ver[1] < distance[ver[0]] and intree[ver[0]] == 0:
                distance[ver[0]] = ver[1]
                parent.pop(ver[0])
                parent.insert(ver[0], v)

        minimum = inf
        for idx in range(len(intree)):
            if intree[idx] == 0:

                if distance[idx] < minimum:
                    minimum = distance[idx]
                    v = idx

        newG.insertEdge(newG.getVertex(parent[v]), newG.getVertex(v), distance[v])
        newG.insertEdge(newG.getVertex(v), newG.getVertex(parent[v]), distance[v])

    return newG, length


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


if __name__ == '__main__':
    graf = graf_mst.graf

    # Struktura
    Gr = AdjacencyList()
    for i in graf:
        if Vertex(i[0]) not in Gr.mapa.keys():
            Gr.insertVertex(Vertex(i[0]))
        if Vertex(i[1]) not in Gr.mapa.keys():
            Gr.insertVertex(Vertex(i[1]))
        Gr.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])
        Gr.insertEdge(Vertex(i[1]), Vertex(i[0]), i[2])

    new, leng = MST(Gr)
    printGraph(new)
