# Skończone
import time

with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()
W = 'time.'

# Naiwna
def naive(S, W):
    counter = 0
    times = 0
    m = 0
    while m != len(S)-1:
        times += 1
        if S[m:m+len(W)] == W:
            counter += 1
        m += 1

    return counter, times

t_start = time.perf_counter()
num_wzorzec, num_porownania = naive(S,W)
t_stop = time.perf_counter()
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(str(num_wzorzec) + ';' + str(num_porownania))

#  Metoda Rabina-Karpa

d = 256
q = 101  # liczba pierwsza


def hash(word):
    hw = 0
    for i in range(len(word)):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw


def RabinKarp(S, W):
    counter = 0
    times = 0
    colision = 0

    M = len(S)
    N = len(W)

    hW = hash(W[:])

    for m in range(M - N + 1):
            hS = hash(S[m:m+N])
            times += 1
            if hS == hW:
                colision += 1
                if S[m:m+N] == W[:]:
                    counter += 1

    return counter, times, colision


t_start = time.perf_counter()
num_wzorzec, num_porownania, kolizje = RabinKarp(S,W)
t_stop = time.perf_counter()
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(str(num_wzorzec) + ';' + str(num_porownania) + ';' + str(kolizje))


# Metoda Knutha-Morrisa-Pratta (KMP)
def kmp_search(S, W):
    m = 0
    i = 0
    counter = 0
    P = [None]*len(W)
    T = kmp_table(W)
    nP = 0
    while m < len(S):
        counter += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                P[nP] = m - i
                nP += 1
                if T[len(W)-1] != -1:
                    i = T[i-1]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1

    return nP, counter

def kmp_table(W):
    pos = 1
    cnd = 0
    T = [None] * len(W)
    T[0] = -1
    while pos < len(W)-1:
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T


num_wzorzec, num_porownania = kmp_search(S,W)
print(str(num_wzorzec) + ';' + str(num_porownania))