#Skończone
import polska


class Vertex:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key


class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.value = 1


class AdjacencyMatrix:
    def __init__(self):
        self.mapa = dict()  # Konwertuje węzeł na jego indeks
        self.lista = []  # Lista z węzłami
        self.matrix = []  # Z indeksami do elementów

    # Dodajemy do listy i jednocześnie do słownika jako wartość słownika
    def insertVertex(self, vertex):
        self.lista.append(vertex)
        idx = self.lista.index(vertex)
        self.mapa[vertex] = idx

        self.matrix.append([0] * len(self.lista))
        for i in range(len(self.lista)-1):
            self.matrix[i].append(0)

    def insertEdge(self, vertex1, vertex2):
        if vertex1 in self.lista and vertex2 in self.lista and vertex1 != vertex2:
            v1 = self.getVertexIdx(vertex1)
            v2 = self.getVertexIdx(vertex2)

            self.matrix[v1][v2] = 1
            self.matrix[v2][v1] = 1

        else:
            raise Exception('Nie ma takiego wierzchołka')

    def deleteVertex(self, vertex):
        if vertex not in self.lista:
            raise Exception('Nie ma takiego wierzchołka')
        else:
            v = self.getVertexIdx(vertex)
            idx = 0
            for i in self.matrix[v]:
                if i == 1:
                    self.deleteEdge(vertex, self.lista[idx])
                idx += 1
            self.matrix.pop(v)
            self.lista.pop(v)
            for i in range(len(self.lista)):
                self.matrix[i].pop(v)

    def deleteEdge(self, vertex1, vertex2):
        if vertex1 in self.lista and vertex2 in self.lista and vertex1 != vertex2:
            v1 = self.getVertexIdx(vertex1)
            v2 = self.getVertexIdx(vertex2)

            self.matrix[v1][v2] = 0
            self.matrix[v2][v1] = 0

    def getVertexIdx(self, vertex):
        return self.mapa[vertex]

    def getVertex(self, vertex_idx):
        return self.lista[vertex_idx]

    def neighbours(self, vertex_idx):
        lista = []
        idx = 0
        for i in self.matrix[vertex_idx]:
            if i == 1:
                lista.append(idx)
            idx += 1
        return lista

    def order(self):
        return len(self.lista)

    def size(self):
        return len(self.edges())

    def edges(self):
        lista = []
        for i in self.lista:
            for k in self.neighbours(self.getVertexIdx(i)):
                lista.append((i.key, self.getVertex(k).key))
        return lista

class AdjacencyList:
    def __init__(self):
        self.mapa = dict()  # Konwertuje węzeł na jego indeks
        self.lista = []  # Lista z węzłami
        self.adjlist = dict()  # Z indeksami do elementów

    def insertVertex(self, vertex):
        self.lista.append(vertex)
        idx = self.lista.index(vertex)
        self.mapa[vertex] = idx
        self.adjlist[idx] = []

    def insertEdge(self, vertex1, vertex2):
        if vertex1 in self.lista and vertex2 in self.lista and vertex1 != vertex2:
            v1 = self.getVertexIdx(vertex1)
            v2 = self.getVertexIdx(vertex2)

            if v1 not in self.adjlist[v2] or v2 not in self.adjlist[v1]:
                self.adjlist[v1].append(v2)
                self.adjlist[v1].sort()

                self.adjlist[v2].append(v1)
                self.adjlist[v2].sort()
        else:
            raise Exception('Nie ma takiego wierzchołka')

    def deleteVertex(self, vertex):
        if vertex in self.lista:
            v = self.getVertexIdx(vertex)
            lista = [i for i in self.adjlist[v]]

            for i in lista:
                self.deleteEdge(vertex, self.getVertex(i))
            self.adjlist.pop(v)

            self.lista.pop(self.getVertexIdx(vertex))
            for x in self.lista:
                self.mapa[x] = self.getVertexIdx(x)

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
        return self.adjlist[vertex_idx]

    def order(self):
        return len(self.lista)

    def size(self):
        return len(self.edges())

    def edges(self):
        lista = []
        for k, v in self.adjlist.items():
            for i in v:
                lista.append((self.getVertex(k).key, self.getVertex(i).key))
        return lista


def DFS(graf, s=0, visited=None):

    if visited is None:
        visited = []

    avcol = ['1', '2', '3', '4', '5']
    colors = dict()
    S = [s]
    while S:
        a = avcol.copy()
        s = S.pop()
        if s not in visited:
            visited.append(s)

            for n in graf.neighbours(s):
                if n in colors.keys():
                    if colors[n] in a:
                        a.remove(colors[n])

            colors[s] = a[0]

            for i in graf.neighbours(s)[::-1]:
                S.append(i)
    return colors


def BFS(graf, s=0, visited=None):

    if visited is None:
        visited = []

    avcol = ['1', '2', '3', '4', '5']
    colors = dict()
    colors[s] = '1'

    Q = [s]
    visited.append(s)
    while Q:
        s = Q.pop(0)

        for n in graf.neighbours(s):
            a = avcol.copy()
            if n not in visited:
                visited.append(n)
                Q.append(n)
                for nn in graf.neighbours(n):
                    if nn in colors.keys():
                        if colors[nn] in a:
                            a.remove(colors[nn])
                colors[n] = a[0]
    return colors


def kolorowanie(graf, typ='DFS'):
    lista = []

    if typ == 'DFS':
        path = DFS(graf)

    elif typ == 'BFS':
        path = BFS(graf)

    else:
        raise Exception('Proszę wprowadzić poprawnie!')

    for k, v in path.items():
        lista.append((graf.getVertex(k).key, v))

    polska.draw_map(graf.edges(), lista)


if __name__ == '__main__':
    G = AdjacencyMatrix()

    for i in polska.graf:
        if Vertex(i[0]) not in G.mapa.keys():
            G.insertVertex(Vertex(i[0]))
        if Vertex(i[1]) not in G.mapa.keys():
            G.insertVertex(Vertex(i[1]))
        G.insertEdge(Vertex(i[0]), Vertex(i[1]))

    # DFS
    kolorowanie(G, 'DFS')

    # BFS
    # kolorowanie(G, 'BFS')

    # Maksymalna liczba kolorów jest taka sama
    