# Skończone

class Element:
    SIZE = 6

    def __init__(self):
        self.tab = [None for _ in range(self.SIZE)]
        self.elem_num = 0
        self.next = None

    def delete(self, idx):
        self.tab[idx] = None
        for t in range(idx, self.elem_num):
            self.tab[t] = self.tab[t+1]
            if t == self.SIZE-2:
                self.tab[t+1] = None
                break
        self.elem_num -= 1

    def add(self, data, idx):
        if idx >= self.elem_num:
            idx = self.elem_num

        else:
            k = None
            for q in range(idx, self.elem_num + 1):
                cur = self.tab[q]
                self.tab[q] = k
                k = cur

        self.tab[idx] = data
        self.elem_num += 1


class UnrolledList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data, idx):
        elem = self.head

        if elem is None:
            self.head = Element()
            self.head.add(data, idx)
        else:

            num = idx
            while num != 0:
                if elem.elem_num == elem.SIZE:
                    elem.elem_num = int(elem.SIZE // 2)
                    nr = elem.elem_num

                    new = Element()

                    for j in range(nr):
                        new.tab[j] = elem.tab[nr + j]
                        new.elem_num += 1

                    for k in range(nr, elem.SIZE):
                        elem.tab[k] = None

                    elem.next = new
                    elem = elem.next

                for i in range(elem.elem_num):
                    num -= 1
                    if num == 0:
                        elem.add(data, i+1)
                        break
                if elem.next is not None:
                    elem = elem.next

    def delete(self, idx):
        elem = self.head
        if elem is None or elem.elem_num == 0:
            raise Exception('Nie można usunąć elementu z pustej tablicy')
        else:
            num = idx
            while num != 0:
                for i in range(elem.elem_num):
                    num -= 1
                    if num == 0:
                        elem.delete(i + 1)
                        break
                if elem.elem_num < int(elem.SIZE // 2):
                    after = elem.next
                    a1 = after.tab[0]
                    after.delete(0)
                    elem.add(a1, 100)
                    if after.elem_num <= 2:
                        for _ in range(2):
                            a1 = after.tab[0]
                            after.delete(0)
                            elem.add(a1, 100)
                        elem.next = after.next
                        del after
                elem = elem.next

    def __str__(self):
        text = '{'
        elem = self.head
        while elem is not None:
            text += '['
            for y in range(elem.SIZE):
                if elem.tab[y] is not None:
                    text += str(elem.tab[y])
                if y + 1 < elem.SIZE and elem.tab[y+1] is not None:
                    text += ', '
            text += ']'
            if elem.next is not None:
                text += ', '
            elem = elem.next
        text += '}'
        return text

    def get(self, idx):
        if self.head is None:
            raise Exception('Pusta lista')
        else:
            num = idx
            elem = self.head
            while num != 0:
                for i in range(elem.elem_num):
                    if num == 0:
                        return elem.tab[i]
                    num -= 1
                elem = elem.next


if __name__ == '__main__':

    # Utworzenie pustej listy
    lista = UnrolledList()

    # Wywołaj w pętli metodę insert do wpisana do listy kolejno 9-ciu danych (kolejnych liczb od 1 do 9)
    for f in range(1, 10):
        lista.insert(f, f-1)

    # Użyj get do wypisania 4-tego elementu listy (numeracja od 0)
    print(lista.get(4))

    # Użyj insert do wstawienia do listy kolejnych 2-ch danych (10 i 11) pod indeksy: 1 i 8
    lista.insert(10, 1)
    lista.insert(11, 8)

    # Wypisz aktualny stan listy
    print(lista)

    # Użyj delete do usunięcia z listy danych spod indeksów 1 i 2
    lista.delete(1)
    lista.delete(2)

    # Wypisz aktualny stan listy
    print(lista)
