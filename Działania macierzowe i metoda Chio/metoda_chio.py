# Skończone
from implementacja_macierzy import Matrix


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


print('Pierwsza macierz M1:')
M1 = Matrix([[5, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])
print(M1)
print(f'Wyznacznik macierzy M1 obliczony metodą Chio wynosi: {chio(M1)}')

print('\nDruga macierz M2:')
M2 = Matrix([[0, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])
print(M2)
print(f'Wyznacznik macierzy M2 obliczony metodą Chio wynosi: {chio(M2)}')
