# Skończone
import random
import time
from copy import deepcopy


def insertion_sort(t):
    tab = deepcopy(t)
    n = len(tab)
    for i in range(1, n):
        first = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > first:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = first
    return tab


def shell(t):
    tab = deepcopy(t)
    N = len(tab)

    k = 1
    while (3 ** k - 1) // 2 <= N // 3:
        h = (3 ** k - 1) // 2
        k += 1

    while h >= 1:
        for i in range(h, N):
            first = tab[i]
            j = i
            while j >= h and tab[j - h] > first:
                tab[j] = tab[j - h]
                j -= h
            tab[j] = first
        h = h // 3
    return tab


def quicksort(t, opp=None):
    tab = deepcopy(t)
    return _quicksort(tab,opp)


def _quicksort(t,opp=None):
    if not t:
        return t
    if opp:
        p = opp
    else:
        p = t[0]

    s = []
    eq = []
    b = []

    for el in t:
        if el < p:
            s.append(el)
        elif el == p:
            eq.append(el)
        elif el > p:
            b.append(el)
    return _quicksort(s) + eq + _quicksort(b)


def magic_fives(t):
    tab = deepcopy(t)
    listy = []
    i = 0
    while len(tab) >= i:
        listy.append(tab[i:i+5])
        i += 5
    n = find_idx(listy)
    return quicksort(tab, n)

def find_idx(listy):
    m = []
    for lista in listy:

        if isinstance(lista, int):
            return lista

        l = len(lista)

        if l == 5:
            m.append(median_5(lista[0], lista[1], lista[2], lista[3], lista[4]))
        elif l == 4:
            m.append(median_4(lista[0], lista[1], lista[2], lista[3]))
        elif l == 3:
            m.append(median_3(lista[0], lista[1], lista[2]))
        else:
            m.append(median_2(lista[0], lista[1]))

        return find_idx(m)

# Pomocnicze
def print_tab(t):
    if t:
        print('{', end=' ')
        for i in range(len(t) - 1):
            if t[i] is not None:
                print(t[i], end=', ')
        if t[len(t) - 1]: print(t[len(t) - 1], end=' ')
        print('}')


def median_2(a, b):
    return (a + b)//2


def median_3(a, b, c):
    return max(min(a, b), min(c, max(a, b)))


def median_4(a, b, c, d):
    return (max(a, b) + min(c, d))//2


def median_5(a, b, c, d, e):
    f = max(min(a, b), min(c, d))  # usuwa najmniejsza z 4
    g = min(max(a, b), max(c, d))  # usuwa największą z 4
    return median_3(e, f, g)


if __name__ == '__main__':
    # Testowanie Insertion Sort
    tablica = [random.randint(0, 100) for _ in range(10000)]

    t_start = time.perf_counter()
    insertion_sort(tablica)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # Testowanie Shell Sort
    t_start = time.perf_counter()
    shell(tablica)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # Shell Sort ma znacznie krótszy czas wykonania niż funkcja Insertion Sort. Jest to wynik, którego się
    # spodziewaliśmy, gdyż Shell Sort miał na celu przyspieszenie drugiej z funkcji. Lepiej od Insertion Sort wypada
    # również HeapSort, który jednak jest wolniejszy od Shell Sort. Obliczenia dla HeapSort zostały przeprowadzone w poprzednym ćwiczeniu
    # i wynosiły zazwyczaj około 0.12 s.

    # -----------------------------------------------------------------
    # Testowanie klasycznego Quicksort
    t_start = time.perf_counter()
    quicksort(tablica)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


    # Testowanie Quicksort (mediana median)
    t_start = time.perf_counter()
    magic_fives(tablica)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # Prawdopodobnie błędy implementacji sprawiły, że funkcja Magic Fice działa nieco wolniej od Quick Sort.
    # Obie funkcje dają jednak bardzo dobre wyniki, w porównaniu do pozostałych funkcji. Prawdopodobnie
    # wynika to z tego, że dostajemy niekorzystne przypadki dla mediany median.