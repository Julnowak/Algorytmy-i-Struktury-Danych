# Skończone
import math
import time
import numpy as np

#  Metoda Rabina-Karpa

d = 256
q = 101  # liczba pierwsza


def hash(word):
    hw = 0
    for i in range(len(word)):  # N - to długość wzorca
        hw = (hw * d + ord(word[
                               i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw


def RabinKarp(S, W):
    counter = 0
    times = 0
    colision = 0

    M = len(S)
    N = len(W)

    hW = hash(W[:])

    for m in range(M - N + 1):
        hS = hash(S[m:m + N])
        times += 1
        if hS == hW:
            colision += 1
            if S[m:m + N] == W[:]:
                counter += 1

    return counter, times, colision

P = 0.001
n = 20

b = -1 * n * math.log(P)/(math.log(2))**2
k = b/n * math.log(2)

def RabinKarpSet(S, subs, N):
    false_positive = 0
    counter = 0
    lis = [0] * int(b)
    hsubs = set()

    slow = dict()

    for sub in subs:
        h = hash(sub[:N])
        hsubs.add(h)
        slow[sub] = 0
        lis[h] = 1
    hs = hash(S[:N])

    for m in range(len(S) - N):
        if lis[hs] == 1 and S[m - 1 : m+N-1] in subs:
            counter += 1
            slow[S[m - 1 : m+N-1]] += 1
        elif hs in hsubs:
            false_positive += 1

        hs = hash(S[m:m+N])
    return counter, false_positive, slow


zbior = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']

with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()

# Standardowo
suma = 0

t_start = time.perf_counter()
for W in zbior:
    num_wzorzec, num_porownania, kolizje = RabinKarp(S,W)
    print(W, num_wzorzec)
    suma += num_wzorzec
print(suma)
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

# Z filtrem Blooma
t_start = time.perf_counter()
c, li, sl = RabinKarpSet(S, zbior, len(zbior[0]))
print(c)
print(li)

t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

for k, v in sl.items():
    print(k, v)
