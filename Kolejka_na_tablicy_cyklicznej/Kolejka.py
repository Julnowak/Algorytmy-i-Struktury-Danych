# Skończone

class Queue:
    def __init__(self, size=5, idx_write=0, idx_read=0):
        tab = [None for _ in range(size)]
        self.tab = tab
        self.size = size
        self.idx_write = idx_write
        self.idx_read = idx_read

    def is_empty(self):
        if self.idx_read == self.idx_write:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.idx_read]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.idx_read += 1

            if self.idx_read == self.size:
                self.idx_read = 0

            val = self.tab[self.idx_read - 1]
            self.tab[self.idx_read - 1] = None
            return val

    def enqueue(self, data):
        self.tab[self.idx_write] = data
        self.idx_write += 1

        if self.idx_write == self.size:
            self.idx_write = self.idx_read

        if self.idx_read == self.idx_write:

            helper = 0
            for i in self.tab:
                if i is None:
                    helper += 1

            self.tab = realloc(self.tab, self.size*2)
            self.tab = self.tab[self.size:] + self.tab[:self.size]
            self.idx_read = self.size + helper
            self.size = self.size * 2
            self.idx_write = 0

    def print_queue(self):
        lista = []
        u = self.idx_read
        for _ in range(len(self.tab)):
            if self.tab[u] is not None:
                lista.append(self.tab[u])
                u += 1
                if u == self.size:
                    u = 0
        print(lista)

    def print_table(self):
        print(self.tab)


def realloc(tab, size):
    oldSize = len(tab)
    return [tab[j] if j < oldSize else None for j in range(size)]


if __name__ == '__main__':

    # Utworzenie pustej listy
    q = Queue()

    # Sprawdzam, czy kolejka jest pusta
    print(f'Czy kolejka jest pusta? {q.is_empty()}\n')

    # Wpisuję do kolejki 4 dane
    for i in range(1, 5):
        q.enqueue(i)

    # Usunięcie i wypisanie danej
    print(f'Wynik odczytu pierwszej wpisanej danej za pomocą "dequeue": {q.dequeue()}\n')

    # Podglądnięcie danej
    print(f'Wynik odczytu pierwszej wpisanej danej za pomocą "peek": {q.peek()}\n')

    # Wypisanie aktualnego stanu kolejki
    print('Aktualny stan kolejki:')
    q.print_queue()

    # Sprawdzam, czy kolejka jest pusta
    print(f'\nCzy kolejka jest pusta? {q.is_empty()}\n')

    # Wpisuję do kolejki następne dane - od 5 do 8
    for i in range(5, 9):
        q.enqueue(i)

    # Wypisanie aktualnego stanu kolejki
    print('Aktualny stan tablicy:')
    q.print_table()

    # Usuwanie elementów w pętli
    print('\nUsunięte dane:')
    while not q.is_empty():
        print(q.dequeue())

    # Wypisanie aktualnego stanu kolejki
    print('\nWypisanie kolejki:')
    q.print_queue()
