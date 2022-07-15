# Skończone
from typing import Tuple, List, Union


class Matrix:
    def __init__(self, entry: Union[Tuple[int, int], List[List]], nums: float = 0):
        # Dla krotek
        if isinstance(entry, Tuple) and len(entry) == 2:
            self.row = entry[0]
            self.column = entry[1]
            r = []
            lista = []

            for i in range(self.row):
                for j in range(self.column):
                    r.append(nums)
                lista.append(r)
                r = []
            self.__matrix = lista

        # Dla list
        elif isinstance(entry, List) and all(isinstance(elem, List) for elem in entry):
            self.row = len(entry)
            self.column = len(entry[0])
            self.__matrix = entry

        else:
            raise Exception('Niepoprawnie wprowadzone dane')

    # Dodawanie
    def __add__(self, other):
        if self.row == other.row and self.column == other.column:
            ans = Matrix((self.row, self.column))

            for i in range(self.row):
                for j in range(self.column):
                    ans[i][j] = self.__matrix[i][j] + other.__matrix[i][j]
            return ans

    # Mnożenie
    def __mul__(self, other):
        if self.column == other.row:
            ans = Matrix((self.row, other.column))

            for i in range(self.row):
                for j in range(other.column):
                    suma = 0
                    for k in range(other.row):
                        suma += self.__matrix[i][k] * other.__matrix[k][j]
                    ans[i][j] = suma
            return ans

        else:
            return None

    def __getitem__(self, item):
        return self.__matrix[item]

    def __str__(self):
        text = ''
        for i in range(self.row):
            text += f'{self.__matrix[i]}\n'
        return text

    # Pytanie o __len__
    def size(self):
        return self.row, self.column


def transpose(matrix: Matrix):
    m = [[0 for _ in range(matrix.row)] for _ in range(matrix.column)]
    for i in range(matrix.row):
        for j in range(matrix.column):
            m[j][i] = matrix[i][j]
    return Matrix(m)


def chio(mat: Matrix):
    if mat.row == mat.column:
        n, _ = mat.size()
        rprop = 0

        while mat[0][0] == 0:
            for i in range(n):
                if mat[i][0] == 0:
                    continue
                else:
                    rprop = i
                    break

            if rprop == 0:
                return 0
            else:
                row1 = mat[0][:]
                row2 = mat[rprop][:]
                mat[0][:] = row2
                mat[rprop][:] = row1

        if n == 1:
            return mat[0][0]
        else:
            b = []
            r = []
            for i in range(n):
                for j in range(n):
                    r.append(0)
                b.append(r)
                r = []
            b = Matrix(b)

            for i in range(0, n):
                for j in range(0, n):
                    b[i][j] = mat[0][0] * mat[i][j] - mat[0][j] * mat[i][0]

            for i in range(b.row):
                b[i].pop(0)
            b = Matrix(b[1:b.row][:])

            if rprop == 0:
                d = 1 / mat[0][0] ** (n - 2) * chio(b)
            else:
                d = -1 / mat[0][0] ** (n - 2) * chio(b)

        return int(d)
    else:
        print('Brak zgodności rozmiarów lub zły rozmiar! Nie można obliczyć wyznacznika.')

if __name__ == '__main__':
    print('Pierwsza macierz M1:')
    M1 = Matrix([[5, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])
    print(M1)
    print(f'Wyznacznik macierzy M1 obliczony metodą Chio wynosi: {chio(M1)}')

    print('\nDruga macierz M2:')
    M2 = Matrix([[0, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])
    print(M2)
    print(f'Wyznacznik macierzy M2 obliczony metodą Chio wynosi: {chio(M2)}')
