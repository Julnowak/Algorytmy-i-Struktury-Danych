# Skończone

import numpy as np
from math import inf

# Wariant rekurencyjny
def string_compare(P, T, i, j):
    if i == 0:
        return len(T[:j])
    if j == 0:
        return len(P[:i])
    if P[i] != T[j]:
        changes = string_compare(P, T, i - 1, j - 1) + 1
    else:
        changes = string_compare(P, T, i - 1, j - 1)
    insertions = string_compare(P, T, i, j - 1) + 1
    deletions = string_compare(P, T, i - 1, j) + 1
    lowest_cost = min(changes, insertions, deletions)
    return lowest_cost


# Wariant PD
def string_compare_PD(P, T):
    D = np.zeros((len(P), len(T)))
    for i in range(len(P)):
        D[i][0] = i
    for j in range(len(T)):
        D[0][j] = j

    parent = np.full((len(P), len(T)),'X')
    for i in range(len(P)):
        if i != 0:
            parent[i][0] = 'D'
    for j in range(len(T)):
        if j != 0:
            parent[0][j] = 'I'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                changes = D[i-1][j-1] + 1
            else:
                changes = D[i-1][j-1]
            insertions = D[i][j-1] + 1
            deletions = D[i-1][j] + 1
            lowest_cost = min(changes, insertions, deletions)
            if P[i] == T[j]:
                parent[i][j] = 'M'
            elif changes <= insertions and changes <= deletions:
                parent[i][j] = 'S'
            elif insertions <= changes and insertions <= deletions:
                parent[i][j] = 'I'
            elif deletions <= changes and deletions <= insertions:
                parent[i][j] = 'D'

            D[i][j] = lowest_cost

    return int(D[-1][-1])

def odtwarzanie(P, T):
    lista = []
    D = np.zeros((len(P), len(T)))
    for i in range(len(P)):
        D[i][0] = i
    for j in range(len(T)):
        D[0][j] = j

    parent = np.full((len(P), len(T)), 'X')
    for i in range(len(P)):
        if i != 0:
            parent[i][0] = 'D'
    for j in range(len(T)):
        if j != 0:
            parent[0][j] = 'I'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                changes = D[i - 1][j - 1] + 1
            else:
                changes = D[i - 1][j - 1]
            insertions = D[i][j - 1] + 1
            deletions = D[i - 1][j] + 1
            lowest_cost = min(changes, insertions, deletions)
            if P[i] == T[j]:
                parent[i][j] = 'M'
                lista.append('M')
            elif changes <= insertions and changes <= deletions:
                parent[i][j] = 'S'
            elif insertions <= changes and insertions <= deletions:
                parent[i][j] = 'I'
            elif deletions <= changes and deletions <= insertions:
                parent[i][j] = 'D'

            D[i][j] = lowest_cost

    lista = []
    idxi = len(P)-1
    idxj = len(T) - 1
    while parent[idxi][idxj] != 'X':
        if parent[idxi][idxj] == 'M':
            idxi -= 1
            idxj -= 1
            lista.append('M')
        elif parent[idxi][idxj] == 'S':
            idxi -= 1
            idxj -= 1
            lista.append('S')
        elif parent[idxi][idxj] == 'I':
            idxj -= 1
            lista.append('I')
        elif parent[idxi][idxj] == 'D':
            idxi -= 1
            lista.append('D')

    return ''.join(lista[::-1])


def dopasowanie(P, T):
    D = np.zeros((len(P), len(T)))
    for i in range(len(P)):
        D[i][0] = i

    parent = np.full((len(P), len(T)), 'X')
    for i in range(len(P)):
        if i != 0:
            parent[i][0] = 'D'


    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                changes = D[i - 1][j - 1] + 1
            else:
                changes = D[i - 1][j - 1]
            insertions = D[i][j - 1] + 1
            deletions = D[i - 1][j] + 1
            lowest_cost = min(changes, insertions, deletions)
            if P[i] == T[j]:
                parent[i][j] = 'M'
            elif changes <= insertions and changes <= deletions:
                parent[i][j] = 'S'
            elif insertions <= changes and insertions <= deletions:
                parent[i][j] = 'I'
            elif deletions <= changes and deletions <= insertions:
                parent[i][j] = 'D'

            D[i][j] = lowest_cost

    idx = goal_cell(P, T, D)

    return idx - (len(P)-2)

def goal_cell(P, T, D):
    i = len(P)-1
    j = 0
    for k in range(1, len(T)):
        if D[i][k] < D[i][j]:
            j = k
    return j


#  Najdłuższa wspólna sekwencja
def common_sec(P,T):
    D = np.zeros((len(P), len(T)))
    for i in range(len(P)):
        D[i][0] = i
    for j in range(len(T)):
        D[0][j] = j

    parent = np.full((len(P), len(T)),'X')
    for i in range(len(P)):
        if i != 0:
            parent[i][0] = 'D'
    for j in range(len(T)):
        if j != 0:
            parent[0][j] = 'I'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                changes = D[i-1][j-1] + inf
            else:
                changes = D[i-1][j-1]
            insertions = D[i][j-1] + 1
            deletions = D[i-1][j] + 1
            lowest_cost = min(changes, insertions, deletions)
            if P[i] == T[j]:
                parent[i][j] = 'M'
            elif changes <= insertions and changes <= deletions:
                parent[i][j] = 'S'
            elif insertions <= changes and insertions <= deletions:
                parent[i][j] = 'I'
            elif deletions <= changes and deletions <= insertions:
                parent[i][j] = 'D'

            D[i][j] = lowest_cost

    string = ''
    for j in range(len(T)):
        for i in range(len(P)):
            if i <= j and parent[i][j] == 'M':
                string += T[j]
    return string

# Najdłuższa podsekwencja monotoniczna
def longest_seq(P,T):
    D = np.zeros((len(P), len(T)))
    for i in range(len(P)):
        D[i][0] = i
    for j in range(len(T)):
        D[0][j] = j

    parent = np.full((len(P), len(T)),'X')
    for i in range(len(P)):
        if i != 0:
            parent[i][0] = 'D'
    for j in range(len(T)):
        if j != 0:
            parent[0][j] = 'I'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                changes = D[i-1][j-1] + inf
            else:
                changes = D[i-1][j-1]
            insertions = D[i][j-1] + 1
            deletions = D[i-1][j] + 1
            lowest_cost = min(changes, insertions, deletions)
            if P[i] == T[j]:
                parent[i][j] = 'M'
            elif changes <= insertions and changes <= deletions:
                parent[i][j] = 'S'
            elif insertions <= changes and insertions <= deletions:
                parent[i][j] = 'I'
            elif deletions <= changes and deletions <= insertions:
                parent[i][j] = 'D'

            D[i][j] = lowest_cost

    string = ''
    for j in range(len(T)):
        for i in range(len(P)):
            if j < i and parent[i][j] == 'M':
                string += T[j]

    return string


if __name__ == '__main__':
    
    # a) wariant rekurencyjny
    P = ' kot'
    T = ' koń'
    print(string_compare(P, T, len(P)-1, len(T)-1))

    P = ' kot'
    T = ' pies'
    print(string_compare(P, T, len(P)-1, len(T)-1))

    # P = ' biały autobus'
    # T = ' czarny autokar'
    # print(string_compare(P, T, len(P) - 1, len(T) - 1))

    # b) wariant PD
    P = ' kot'
    T = ' koń'
    print(string_compare_PD(P, T))

    P = ' kot'
    T = ' pies'
    print(string_compare_PD(P, T))

    P = ' biały autobus'
    T = ' czarny autokar'
    print(string_compare_PD(P, T))

    # c) odtwarzanie ścieżki
    P = ' thou shalt not'
    T = ' you should not'
    print(odtwarzanie(P, T))

    # d) dopasowanie podciągów
    P = ' ban'
    T = ' mokeyssbanana'
    print(dopasowanie(P, T))
    # Słówko bin również zostało wyszukane
    
    # e) najdłuższa wspólna sekwencja
    P = ' democrat'
    T = ' republican'
    print(common_sec(P, T))

    # f) najdłuższa podsekwencja monotoniczna
    T = ' 243517698'

    lista = []
    for s in T.lstrip():
        lista.append(int(s))
    lista.sort()

    P = " "
    for v in lista:
        P += str(v)

    print(longest_seq(P, T))
