# Skończone
from random import random


class Element:
    def __init__(self, key=None, data=None, lvl=0):
        self.key = key
        self.data = data
        self.lvl = lvl
        self.next = [None] * (lvl+1)


class SkipList:
    def __init__(self, maxLevel=5):
        self.maxLevel = maxLevel
        self.head = Element(None, None, self.maxLevel)

    def randomLevel(self, p=0.5):
        lvl = 0
        while random() < p and lvl < self.maxLevel:
            lvl = lvl + 1
        return lvl

    def search(self, key):
        if isinstance(key, int):
            node = self.head.next[0]
            while node is not None:
                if node.key == key:
                    return node.data
                node = node.next[0]
            raise Exception('Nie ma takiego klucza')
        else:
            raise Exception('Źle wprowadzony klucz')

    def insert(self, key, data):
        if isinstance(key, int):
            previous = [None] * (self.maxLevel+1)
            node = self.head
            my_lvl = self.maxLevel-1

            for i in range(my_lvl, -1, -1):
                while node.next[i] is not None and node.next[i].key < key:
                    node = node.next[i]
                previous[i] = node
            node = node.next[0]

            if node is None or node.key != key:
                rand_lvl = self.randomLevel()

                if rand_lvl > my_lvl:
                    for i in range(my_lvl, rand_lvl+1):
                        previous[i] = self.head
                    my_lvl = rand_lvl

                elem = Element(key, data, rand_lvl)

                for n in range(rand_lvl+1):
                    elem.next[n] = previous[n].next[n]
                    previous[n].next[n] = elem

            elif node.key == key:
                node.data = data

            for p in range(len(previous)):
                if previous[p] is None:
                    previous[p] = self.head
            return previous
        else:
            raise Exception('Źle wprowadzony klucz')

    def remove(self, key):
        if isinstance(key, int):
            previous = [None] * self.maxLevel
            node = self.head
            my_lvl = self.maxLevel-1

            for i in range(my_lvl, -1, -1):
                while node.next[i] is not None and node.next[i].key < key:
                    node = node.next[i]
                previous[i] = node

            node = node.next[0]

            if node is not None and node.key == key:
                for y in range(my_lvl + 1):
                    if previous[y].next[y] != node:
                        break
                    previous[y].next[y] = node.next[y]

                if self.head.next[my_lvl] is None and my_lvl > 0:
                    my_lvl -= 1
            else:
                raise Exception('Nie ma takiego klucza')
        else:
            raise Exception('Źle wprowadzony klucz')

    def __str__(self):
        node = self.head.next[0]
        keys = []
        vals = []
        while node is not None:
            keys.append(node.key)
            vals.append(node.data)
            node = node.next[0]
        text = '['
        for i in range(len(keys)):
            text += f'({keys[i]}:{vals[i]})'
            if i == len(keys)-1:
                text += ']'
            else:
                text += ', '
        return text

    def displayList_(self):
        node = self.head.next[0]
        keys = []
        while node is not None:
            keys.append(node.key)
            node = node.next[0]

        for lvl in range(self.maxLevel - 1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.next[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print("  ", end=" ")
                    idx += 1
                idx += 1
                print("{:2d}".format(node.key), end=" ")
                node = node.next[lvl]
            print("")


if __name__ == '__main__':

    # Utworzenie pustej listy
    lista = SkipList()

    # użycie insert do wpisana do niej 15 danych
    # (niech kluczami będą kolejne liczby od 1, a wartościami - kolejne litery),

    keys1 = list(range(1, 16))
    values1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

    for k in keys1:
        lista.insert(k, values1[k-1])

    # Wypisanie listy
    print(lista)

    # Użycie search do wyszukania (i wypisania) danej o kluczu 2
    print(lista.search(2))

    # Użycie insert do nadpisania wartości dla klucza 2 literą 'Z'
    lista.insert(2, 'Z')

    # Użycie search do wyszukania (i wypisania) danej o kluczu 2
    print(lista.search(2))

    # Użycie delete do usunięcia danych o kluczach 5, 6, 7
    lista.remove(5)
    lista.remove(6)
    lista.remove(7)

    # Wypisanie tablicy
    lista.displayList_()

    # Użycie insert do wstawienia danej 'W' o kluczu 6
    lista.insert(6, 'W')

    # Wypisanie tablicy
    lista.displayList_()
    ##################################

    # Utworzenie pustej listy
    lista2 = SkipList()

    # użycie insert do wpisana do niej 15 danych
    # (niech kluczami będą kolejne liczby od 1, a wartościami - kolejne litery),
    keys2 = list(range(15, 0, -1))
    values2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    helper = 0

    for k in keys2:
        lista2.insert(k, values2[helper])
        helper += 1

    # Wypisanie listy
    print(lista2)

    # Użycie search do wyszukania (i wypisania) danej o kluczu 2
    print(lista2.search(2))

    # Użycie insert do nadpisania wartości dla klucza 2 literą 'Z'
    lista2.insert(2, 'Z')

    # Użycie search do wyszukania (i wypisania) danej o kluczu 2
    print(lista2.search(2))

    # Użycie delete do usunięcia danych o kluczach 5, 6, 7
    lista2.remove(5)
    lista2.remove(6)
    lista2.remove(7)

    # Wypisanie tablicy
    lista2.displayList_()

    # Użycie insert do wstawienia danej 'W' o kluczu 6
    lista2.insert(6, 'W')

    # Wypisanie tablicy
    lista2.displayList_()
