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
        ans = []
        if self.row == other.row and self.column == other.column:
            r = []
            for i in range(self.row):
                for j in range(self.column):
                    r.append(0)
                ans.append(r)
                r = []

            for i in range(self.row):
                for j in range(self.column):
                    ans[i][j] = self.__matrix[i][j] + other.__matrix[i][j]
            return Matrix(ans)

    # Mnożenie
    def __mul__(self, other):
        if self.column == other.row:
            ans = []
            r = []
            for i in range(self.row):
                for j in range(other.column):
                    r.append(0)
                ans.append(r)
                r = []

            for i in range(self.row):
                for j in range(other.column):
                    suma = 0
                    for k in range(other.row):
                        suma += self.__matrix[i][k] * other.__matrix[k][j]
                    ans[i][j] = suma
            return Matrix(ans)

        else:
            return 'Nie można pomnożyć macierzy'

    def __getitem__(self, item):
        return self.__matrix[item]

    def __str__(self):
        text = ''
        for i in range(self.row):
            text += f'{self.__matrix[i]}\n'
        return text

    def size(self):
        return self.row, self.column


def transpose(matrix: Matrix):
    m = [[0 for _ in range(matrix.row)] for _ in range(matrix.column)]
    for i in range(matrix.row):
        for j in range(matrix.column):
            m[j][i] = matrix[i][j]
    return Matrix(m)


if __name__ == '__main__':
    print('Macierze z zadania:')

    M1 = Matrix([[1, 0, 2], [-1, 3, 1]])
    print(f'-> Macierz M1 (utworzona za pomocą listy list):\n{M1}')

    M2 = Matrix((2, 3), nums=1)
    print(f'-> Macierz M2 (utworzona poprzez podanie rozmiarów macierzy i parametru nums=1):\n{M2}')

    M3 = Matrix([[3, 1], [2, 1], [1, 0]])
    print(f'-> Macierz M3 (utworzona za pomocą listy list):\n{M3}\n')

    # Transpozycja macierzy
    print(f'Transpozycja macierzy M1:\n{transpose(M1)}')

    # Sumowanie obu macierzy
    print(f'Wynik sumowania macierzy M1 i M2:\n{M1 + M2}')

    # Mnożenie macierzowe obu macierzy
    print(f'Wynik mnożenia macierzy M1 i M3:\n{M1 * M3}')
    print(f'Wynik mnożenia macierzy M3 i M1:\n{M3 * M1}')
