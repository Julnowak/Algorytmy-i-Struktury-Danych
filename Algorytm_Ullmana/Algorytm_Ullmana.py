# Skończone
import numpy as np


class Vertex:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key


class Edge:
    def __init__(self, vertex1, vertex2, weight=1):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight


class AdjacencyMatrix:
    def __init__(self):
        self.mapa = dict()  # Konwertuje węzeł na jego indeks
        self.lista = []  # Lista z węzłami
        self.matrix = []  # Z indeksami do elementów
        self.edges = dict()  #

    def insertVertex(self, vertex):
        if vertex in self.lista:
            raise Exception('Węzeł już istnieje')
        self.lista.append(vertex)
        idx = self.lista.index(vertex)
        self.mapa[vertex] = idx

        self.matrix.append([0] * len(self.lista))
        for h in range(len(self.lista) - 1):
            self.matrix[h].append(0)


    def insertEdge(self, vertex1, vertex2, weight=1):
        if vertex1 in self.lista and vertex2 in self.lista and vertex1 != vertex2:
            v1 = self.getVertexIdx(vertex1)
            v2 = self.getVertexIdx(vertex2)

            self.matrix[v1][v2] = weight
            self.edges[(v1, v2)] = Edge(vertex1, vertex2, weight)

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
        return len(self.list_of_edges()) // 2

    def list_of_edges(self):
        lista = []
        for i in self.lista:
            for k in self.neighbours(self.getVertexIdx(i)):
                lista.append((i.key, self.getVertex(k).key))
        return lista

    def takeMatrix(self):
        return np.array(self.matrix)

    def EdgesOfVertex(self, vertex):
        lista = []
        idx = self.getVertexIdx(vertex)
        for key, val in self.edges.items():
            if key[0] == idx:
                lista.append(val)
        return lista


def Ullman1(curRow, G, P, M, no_recursion=0, counter=0, usedCols=None):
    if usedCols is None:
        usedCols = []

    rows = M.shape[0]
    cols = M.shape[1]

    no_recursion += 1
    if curRow == rows:
        if isIsomorphic(M, G, P):
            counter += 1
            return True, no_recursion, M, counter

    unusedCols = []
    for column in range(cols):
        if column not in usedCols:
            unusedCols.append(column)

    for c in unusedCols:
        try:
            for i in range(cols):
                M[curRow][c] = 1
                if i != c:
                    M[curRow][i] = 0

            usedCols.append(c)
            _, no_recursion, M, counter = Ullman1(curRow + 1, G, P, M, no_recursion, counter, usedCols)
            usedCols.remove(c)
        except:
            pass

    return False, no_recursion, M, counter


def Ullman2(curRow, G, P, M, M0, no_recursion=0, counter=0, usedCols=None):
    if usedCols is None:
        usedCols = []

    rows = M.shape[0]
    cols = M.shape[1]

    no_recursion += 1
    if curRow == rows:
        if isIsomorphic(M, G, P):
            counter += 1
            return True, no_recursion, M, counter

    unusedCols = []
    for column in range(cols):
        if column not in usedCols:
            unusedCols.append(column)

    for c in unusedCols:
        try:
            if M0[curRow][c] == 1:
                for i in range(cols):
                    M[curRow][c] = 1
                    if i != c:
                        M[curRow][i] = 0

                usedCols.append(c)
                _, no_recursion, M, counter = Ullman2(curRow + 1, G, P, M, M0, no_recursion, counter, usedCols)
                usedCols.remove(c)
        except:
            pass

    return False, no_recursion, M, counter


def Ullman3(curRow, G, P, M, M0, no_recursion=0, counter=0, usedCols=None):
    if usedCols is None:
        usedCols = []

    rows = M.shape[0]
    cols = M.shape[1]

    no_recursion += 1
    if curRow == rows:
        if isIsomorphic(M, G.takeMatrix(), P.takeMatrix()):
            counter += 1
            return True, no_recursion, M, counter

    Mp = M.copy()

    unusedCols = []
    for column in range(M.shape[1]):
        if column not in usedCols:
            unusedCols.append(column)

    prune(Mp, G, P)

    if not np.any([np.array_equal(Mp[n], Mp.shape[1] * [0]) for n in range(Mp.shape[0])]):
        for c in unusedCols:
            if M0[curRow][c] == 1:
                for f in range(cols):
                    Mp[curRow][c] = 1
                    if f != c:
                        Mp[curRow][f] = 0
                usedCols.append(c)
                _, no_recursion, M, counter = Ullman3(curRow + 1, G, P, Mp, M0, no_recursion, counter, usedCols)
                usedCols.remove(c)

    return False, no_recursion, M, counter


def isIsomorphic(M, newG, newP):
    new = np.matmul(M, np.transpose(np.matmul(M, newG)))
    for i in range(newP.shape[0]):
        for j in range(newP.shape[1]):
            if newP[i][j] != new[i][j]:
                return False
    return True


def prune(B, G, P):
    flaga = True
    temp = B
    while flaga:
        for i in range(B.shape[0]):
            for j in range(B.shape[1]):
                if B[i][j] == 1:
                    for x in P.neighbours(i):
                        rem = None
                        for y in G.neighbours(j):
                            if B[x][y] == 1:
                                rem = y
                        if rem:
                            B[i][j] = 1
                        else:
                            B[i][j] = 0
                            break

        if np.array_equal(temp, B):
            flaga = False
        else:
            temp = B


if __name__ == '__main__':
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

    G = AdjacencyMatrix()
    for i in graph_G:
        if not Vertex(i[0]) in G.mapa.keys():
            G.insertVertex(Vertex(i[0]))
        if not Vertex(i[1]) in G.mapa.keys():
            G.insertVertex(Vertex(i[1]))
        G.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])
        G.insertEdge(Vertex(i[1]), Vertex(i[0]), i[2])

    P = AdjacencyMatrix()
    for i in graph_P:
        if not Vertex(i[0]) in P.mapa.keys():
            P.insertVertex(Vertex(i[0]))
        if not Vertex(i[1]) in P.mapa.keys():
            P.insertVertex(Vertex(i[1]))
        P.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])
        P.insertEdge(Vertex(i[1]), Vertex(i[0]), i[2])

    MG = np.array(G.matrix)
    MP = np.array(P.matrix)

    # Ullman wersja 1.0
    M = np.zeros((P.order(), G.order()))
    _, num, mat, co = Ullman1(0, MG, MP, M)
    print(co, num)

    # Ullman wersja 2.0
    M = np.zeros((P.order(), G.order()))
    M0 = np.zeros((MP.shape[0], MG.shape[0]))
    for i in range(M.shape[1]):
        for j in range(M.shape[0]):
            if len(G.EdgesOfVertex(G.getVertex(i))) >= len(P.EdgesOfVertex(P.getVertex(j))):
                M0[j][i] = 1
            else:
                M0[j][i] = 0

    _, num2, mat2, co2 = Ullman2(0, MG, MP, M, M0)
    print(co2, num2)


    # Ullman wersja 3.0
    M = np.zeros((MP.shape[0], MG.shape[0]))
    M0 = np.zeros((MP.shape[0], MG.shape[0]))
    for i in range(M.shape[1]):
        for j in range(M.shape[0]):
            if len(G.EdgesOfVertex(G.getVertex(i))) >= len(P.EdgesOfVertex(P.getVertex(j))):
                M0[j][i] = 1
            else:
                M0[j][i] = 0

    M = np.ones((MP.shape[0], MG.shape[0]))
    _, num3, mat3, co3 = Ullman3(0, G, P, M, M0)
    print(co3, num3)
