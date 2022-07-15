# Skończone

# Funkcja realloc została nieco inaczej wykorzystana niż przy tablicy cyklicznej,
# dzięki czemu, jej działanie bardziej przypomina listę pythonowską i ułatwia prowadzenie działań

def realloc(tab, size):
    oldSize = len(tab)
    return [tab[j] if j < oldSize else None for j in range(size)]


class Element:
    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __str__(self):
        return f'{self.priority} : {self.data}'

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority


class MaxHeap:
    def __init__(self, size):
        self.size = size
        self.tab = [None for _ in range(size)]
        self.height = 0

    def print_tab(self):
        print('{', end=' ')
        for i in range(self.size-1):
            if self.tab[i] is not None:
                print(self.tab[i], end = ', ')
        if self.tab[self.size-1]: print(self.tab[self.size-1], end = ' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else '')
            self.print_tree(self.left(idx), lvl+1)

    def is_empty(self):
        if any(self.tab):
            return False
        return True

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[0]

    def dequeue(self):
        idx = self.height-1
        if self.is_empty():
            return None
        else:
            ans = self.tab[0]
            if self.height == 1:
                self.tab[0] = None
            else:
                h = self.tab[idx]
                self.tab[idx] = None
                self.tab[0] = h
                m = 0
                while self.tab[self.left(m)] is not None or self.tab[self.right(m)] is not None:
                    if self.tab[self.left(m)] is not None and self.tab[self.right(m)] is not None:
                        if self.tab[self.left(m)].priority > self.tab[self.right(m)].priority:
                            h1 = self.tab[self.left(m)]
                            self.tab[self.left(m)] = self.tab[m]
                            self.tab[m] = h1
                            m = self.tab.index(self.tab[self.left(m)])
                        else:
                            h2 = self.tab[self.right(m)]
                            self.tab[self.right(m)] = self.tab[m]
                            self.tab[m] = h2
                            m = self.tab.index(self.tab[self.right(m)])
                    elif self.tab[self.left(m)] is not None:
                        h1 = self.tab[self.left(m)]
                        self.tab[self.left(m)] = self.tab[m]
                        self.tab[m] = h1
                        m = self.tab.index(self.tab[self.left(m)])
                    else:
                        h2 = self.tab[self.right(m)]
                        self.tab[self.right(m)] = self.tab[m]
                        self.tab[m] = h2
                        m = self.tab.index(self.tab[self.right(m)])

                    if self.left(m) > self.height or self.right(m) > self.height:
                        break
        return ans

    def enqueue(self, priority, data):
        idx = self.height
        if self.is_empty():
            self.tab[idx] = Element(priority, data)
        else:
            self.tab[idx] = Element(priority, data)

            while self.tab[idx].priority > self.tab[self.parent(idx)].priority:
                h1 = self.tab[idx]
                h2 = self.tab[self.parent(idx)]
                self.tab[idx] = h2
                self.tab[self.parent(idx)] = h1
                idx = self.parent(idx)

                if self.tab[idx] is None or self.tab[self.parent(idx)] is None:
                    break
        self.height += 1

        if self.height == self.size:
            self.tab = realloc(self.tab, self.size * 2)
            self.size = self.size * 2


    def left(self, idx):
        return 2*(idx+1)-1

    def right(self, idx):
        return 2*(idx+1)

    def parent(self, idx):
        return (idx-1)//2


if __name__ == '__main__':

    # Utworzenie pustej kolejki
    Q = MaxHeap(8)

    # Użycie w pętli enqueue do wpisana do niej elementów których klucze będą brane z listy [4, 7, 6, 7, 5, 2, 2, 1]
    # a odpowiadające im wartości będą kolejnymi literami z napisu "ALGORYTM"

    keys = [4, 7, 6, 7, 5, 2, 2, 1]
    values = "ALGORYTM"
    for i in range(len(keys)):
        Q.enqueue(keys[i], values[i])

    # Wypisanie aktualnego stanu kolejki w postaci kopca
    Q.print_tree(0, 0)

    # Wypisanie aktualnego stanu kolejki w postaci tablicy
    Q.print_tab()

    # Użycie dequeue do odczytu (i wypisania) pierwszej danej z kolejki
    print(Q.dequeue())

    # Użycie peek do odczytu (i wypisania) kolejnej danej
    print(Q.peek())

    # Wypisanie aktualnego stanu kolejki w postaci tablicy
    Q.print_tab()

    # Opróżnienie kolejki z wypisaniem usuwanych danych (użycie dequeue w pętli dopóki w kolejce będą dane)
    while Q.is_empty() is False:
        print(Q.dequeue())

    # Wypisanie opróżnionej kolejki w postaci kopca (powinno się wypisać { } )
    Q.print_tab()
