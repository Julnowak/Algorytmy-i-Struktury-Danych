# Skończone

class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        tab = [None for _ in range(size)]
        self.tab = tab
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def hash(self, key):
        if isinstance(key, str):
            suma = 0
            for letter in key:
                suma += ord(letter)
            key = suma
        return key % self.size

    def collision(self, hashed_key):
        for i in range(self.size):
            place = (hashed_key + self.c1 * i + self.c2 * i ** 2) % self.size
            if self.tab[place] is None:
                return place
        return None

    def search(self, ki):
        for i in range(self.size):
            if self.tab[i] is None:
                continue
            elif self.tab[i].key == ki:
                return self.tab[i].data
        return None

    def insert(self, ki, d):
        key = self.hash(ki)
        idx = self.collision(key)
        if idx is None:
            keys = [self.tab[num].key for num in range(self.size) if self.tab[num] is not None]
            if ki in keys:
                self.tab[ki].key = ki
                self.tab[ki].data = d
            else:
                print("Brak miejsca")
                return None
        else:
            self.tab[idx] = Element(key=ki, data=d)

    def remove(self, ki):
        idx = self.hash(ki)
        if self.tab[idx] is None:
            print("Brak danej")
            return None
        self.tab[idx] = None

    def __str__(self):
        text = '{'
        for i in range(self.size):
            if self.tab[i] is None:
                if i == self.size - 1:
                    text += 'None}'
                else:
                    text += 'None, '
            else:
                if i == self.size - 1:
                    text += f'{self.tab[i].key}:{self.tab[i].data}' + '}'
                else:
                    text += f'{self.tab[i].key}:{self.tab[i].data}, '
        return text


def test_fun_1(size, c1, c2):
    # Utworzenie pustej tablicy o rozmiarze 13 i próbkowaniem liniowym
    H = HashTable(size, c1=c1, c2=c2)

    # użycie insert do wpisana do niej 15 danych Niech kluczami będą  kolejne liczby od 1
    # (ZA WYJĄTKIEM 6 i 7, zamiast których kluczami powinny być 18 i 31), a wartościami
    # - kolejne litery od 'A'.
    keys = [1, 2, 3, 4, 5, 18, 31, 8, 9, 10, 11, 12, 13, 14, 15]
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for k in keys:
        H.insert(k, values[keys.index(k)])

    # Wypisanie tablicy
    print(H)

    # Użycie search do wyszukania (i wypisania) danej o kluczu 5
    print(H.search(5))

    # Użycie search do wyszukania (i wypisania) danej o kluczu 14
    print(H.search(14))

    # Użycie insert do nadpisania wartości dla klucza 5 wartością 'Z'
    H.insert(5, 'Z')

    # Użycie search do wyszukania (i wypisania) danej o kluczu 5
    print(H.search(5))

    # Użycie remove do usunięcia danej o kluczu 5
    H.remove(5)

    # Wypisanie tablicy
    print(H)

    # Użycie search do wyszukania (i wypisania) danej o kluczu 31
    print(H.search(31))

    # Wprowadź do tablicy insertem daną o wartości 'W' z kluczem 'test' i ponownie wypisz tablicę.
    H.insert('test', 'W')
    print(H)


def test_fun_2(size, c1, c2):
    H = HashTable(size, c1=c1, c2=c2)
    keys = [13 * n for n in range(1, 16)]
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

    for k in keys:
        H.insert(k, values[keys.index(k)])

    print(H)


if __name__ == '__main__':

    test_fun_1(13, 1, 0)

    test_fun_2(13, 1, 0)

    test_fun_2(13, 0, 1)

    test_fun_1(13, 0, 1)
