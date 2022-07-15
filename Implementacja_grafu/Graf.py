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

    def insertVertex(self, vertex):
        if vertex in self.lista:
            raise Exception('Węzeł już istnieje')
        self.lista.append(vertex)
        idx = self.lista.index(vertex)
        self.mapa[vertex] = idx

        self.matrix.append([0] * len(self.lista))
        for h in range(len(self.lista)-1):
            self.matrix[h].append(0)

    def insertEdge(self, vertex1, vertex2):
        if vertex1 in self.lista and vertex2 in self.lista and vertex1 != vertex2:
            v1 = self.getVertexIdx(vertex1)
            v2 = self.getVertexIdx(vertex2)

            self.matrix[v1][v2] = 1
            self.matrix[v2][v1] = 1

        else:
            raise Exception('Źle dobrane wierzchołki')

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
            self.mapa.pop(vertex)
            for t in range(len(self.lista)):
                self.matrix[t].pop(v)
                self.mapa[self.lista[t]] = t

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
        for y in self.matrix[vertex_idx]:
            if y == 1:
                lista.append(idx)
            idx += 1
        return lista

    def order(self):
        return len(self.lista)

    def size(self):
        return len(self.edges())//2

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
        if vertex in self.lista:
            raise Exception('Węzeł już istnieje')
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
            print(v)
            lista = [i for i in self.adjlist[v]]

            for i in lista:
                self.deleteEdge(vertex, self.getVertex(i))

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
        return self.adjlist[vertex_idx]

    def order(self):
        return len(self.lista)

    def size(self):
        return len(self.edges())//2

    def edges(self):
        lista = []
        for k, v in self.adjlist.items():
            for i in v:
                lista.append((self.getVertex(k).key, self.getVertex(i).key))
        return lista


if __name__ == '__main__':
    # Na początek należy stworzyć graf korzystając z podanej listy krawędzi (z użyciem metod insertVertex i insertEdge).
    # G = AdjacencyList()
    G = AdjacencyMatrix()

    for i in polska.graf:
        if Vertex(i[0]) not in G.mapa.keys():
            G.insertVertex(Vertex(i[0]))
        if Vertex(i[1]) not in G.mapa.keys():
            G.insertVertex(Vertex(i[1]))
        G.insertEdge(Vertex(i[0]), Vertex(i[1]))

    # Następnie należy usunąć z grafu województwo małopolskie (deleteVertex)
    G.deleteVertex(Vertex('K'))

    # Następnie należy usunąć z grafu  połączenia między mazowieckim i łódzkimi (deleteEdge).
    G.deleteEdge(Vertex('W'), Vertex('E'))

    # Poprawność należy sprawdzić przez wyświetlenie stworzonych grafów (draw_map)
    polska.draw_map(G.edges())
