# Skończone
import random
import time


def realloc(tab, size):
    oldSize = len(tab)
    return [tab[j] if j < oldSize else None for j in range(size)]


class Element:
    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __str__(self):
        return f'{self.priority}:{self.data}'

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority


class Heap:
    def __init__(self, tab_size, to_be_sorted=None):
        if to_be_sorted is None:
            self.tab = [None for _ in range(tab_size)]
            self.TAB_SIZE = tab_size
            self.size = 0

        elif isinstance(to_be_sorted, list):
            self.tab = to_be_sorted
            self.size = len(to_be_sorted)

    def print_tab(self):
        print('{', end=' ')
        for i in range(self.size - 1):
            if self.tab[i] is not None:
                print(self.tab[i], end=', ')
        if self.tab[self.size - 1]: print(self.tab[self.size - 1], end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else '')
            self.print_tree(self.left(idx), lvl + 1)

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
        idx = self.size - 1
        if self.is_empty():
            return None
        else:
            ans = self.tab[0]
            if self.size == 1:
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
                            m = self.left(m)
                        else:
                            h2 = self.tab[self.right(m)]
                            self.tab[self.right(m)] = self.tab[m]
                            self.tab[m] = h2
                            m = self.right(m)
                    elif self.tab[self.left(m)] is not None:
                        h1 = self.tab[self.left(m)]
                        self.tab[self.left(m)] = self.tab[m]
                        self.tab[m] = h1
                        m =self.left(m)
                    else:
                        h2 = self.tab[self.right(m)]
                        self.tab[self.right(m)] = self.tab[m]
                        self.tab[m] = h2
                        m = self.right(m)

                    if self.left(m) > self.size or self.right(m) > self.size:
                        break
        self.size -= 1
        if self.size == self.TAB_SIZE//2 - 1:
            self.tab = realloc(self.tab, self.TAB_SIZE//2)
            self.TAB_SIZE = self.TAB_SIZE // 2
        return ans

    def enqueue(self, priority, data):
        idx = self.size
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
        self.size += 1

        if self.size == self.TAB_SIZE:
            self.tab = realloc(self.tab, self.TAB_SIZE * 2)
            self.TAB_SIZE = self.TAB_SIZE * 2

    def left(self, idx):
        return 2 * (idx + 1) - 1

    def right(self, idx):
        return 2 * (idx + 1)

    def parent(self, idx):
        return (idx - 1) // 2

    def heapify(self):
        idx = self.size-1
        parents = list(range(self.parent(self.size), -1, -1))

        for parent in parents:
            m = parent
            if self.left(parent) < self.size and self.tab[m] < self.tab[self.left(parent)]:
                m = self.left(parent)

            if self.right(parent) < self.size and self.tab[m] < self.tab[self.right(parent)]:
                m = self.right(parent)

            if m != parent:
                h = self.tab[parent]
                self.tab[parent] = self.tab[m]
                self.tab[m] = h
                self._heapify(self.tab, self.size, m)

        for i in range(idx, 0, -1):
            h = self.tab[i]
            self.tab[i] = self.tab[0]
            self.tab[0] = h
            m = 0
            if self.left(0) < i and self.tab[m] < self.tab[self.left(0)]:
                m = self.left(0)

            if self.right(0) < i and self.tab[m] < self.tab[self.right(0)]:
                m = self.right(0)

            if m != 0:
                h = self.tab[0]
                self.tab[0] = self.tab[m]
                self.tab[m] = h
                self._heapify(self.tab, i, m)

    def _heapify(self, tab, size, par):
        m = par
        if self.left(par) < size and tab[m] < tab[self.left(par)]:
            m = self.left(par)

        if self.right(par) < size and tab[m] < tab[self.right(par)]:
            m = self.right(par)

        if m != par:
            h = tab[par]
            tab[par] = tab[m]
            tab[m] = h
            self._heapify(tab, size, m)


def print_tab(t):
    if t:
        print('{', end=' ')
        for i in range(len(t) - 1):
            if t[i] is not None:
                print(t[i], end=', ')
        if t[len(t) - 1]: print(t[len(t) - 1], end=' ')
        print('}')


def swap(t):
    tab = t.copy()
    n = len(tab)
    for i in range(n - 1):
        m = tab.index(min(tab[i:]))
        s = tab[i]
        tab[i] = tab[m]
        tab[m] = s
    return tab


def shift(t):
    tab = t.copy()
    n = len(tab)
    for i in range(n - 1):
        m = tab.index(min(tab[i:]))
        s = tab.pop(m)
        tab.insert(i, s)
    return tab


if __name__ == '__main__':
    # Sortowanie z wykorzystaniem kopca
    l = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]

    tablica = []
    for i in range(len(l)):
        tablica.append(Element(l[i][0], l[i][1]))

    Q = Heap(10, tablica)
    Q.print_tab()
    Q.heapify()

    Q.print_tree(0,0)
    Q.print_tab()


    tab2 = [int(random.random() * 100) for _ in range(10000)]
    Q1 = Heap(10, tab2)
    t_start = time.perf_counter()
    Q1.heapify()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # OBSERWACJA
    # Sortowanie przy pomocy kopca jest niestabilne, gdyż nie wszystkie elementy zachowały swoją kolejność

    # Sortowanie przez wybieranie

    l = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]

    tablica = []
    for i in range(len(l)):
        tablica.append(Element(l[i][0], l[i][1]))

    # Metoda Swap
    # print_tab(tablica)
    new = swap(tablica)
    print_tab(new)

    # Metoda Shift
    # print_tab(tablica)
    new_tab = shift(tablica)
    print_tab(new_tab)

    # OBSERWACJA STABILNOŚCI
    # Metoda swap() jest metodą niestabilną, o czym świadczy fakt, że kolejność elementów z listy początkowej
    # nie zawsze jest zachowana np. wartość 5:E powinna znaleźć się na liście później niż 5:A
    # Metoda shift() jest natomiast przekształconą formą standardowego Selection Sort, która nadaje metodzie
    # stabilność - kolejność elementów w liście początkowej jest zachowana

    tab3 = [random.randint(0, 1000) for _ in range(10000)]
    t_start = time.perf_counter()
    new = swap(tab3)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    new_tab = shift(tab3)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # Każdorazowo czas obliczeń dla metody shift() jest dłuższy od metody swap()
    # Czas obliczeń obu metod jest dłuższy od sortowania przy pomocy kopca
