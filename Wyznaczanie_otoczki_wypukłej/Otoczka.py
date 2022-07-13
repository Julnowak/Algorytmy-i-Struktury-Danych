# Skończone
import math
from math import inf


def check_skretp(p, q, r):
    x1, y1 = p
    x2, y2 = q
    x3, y3 = r

    if (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1) > 0:
        return True     # Prawo
    elif (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1) == 0:
        return False   # Współ
    elif (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1) < 0:
        return False     # Lewo


def check_skretw(p, q, r):
    x1, y1 = p
    x2, y2 = q
    x3, y3 = r

    if (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1) > 0:
        return False    # Prawo
    elif (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1) == 0:
        return True   # Współ
    elif (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1) < 0:
        return False     # Lewo

def dist(p1,p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def otoczkaI(zbior):
    lis =[]
    p = (inf, inf)
    for point in zbior:
        if point[0] < p[0]:
            p = point
        elif point[0] == p[0]:
            if point[1] < p[1]:
                p = point


    lis.append(p)
    copyP = p

    flaga = True
    while flaga:
        if zbior.index(p)+1 >= len(zbior):
            q = zbior[0]
        else:
            q = zbior[zbior.index(p)+1]       # Ograniczenie trzeba
        for r in zbior:
            if r != p and r != q:
                ans = check_skretp(p, q, r)
                if ans:
                    q = r

        if q == copyP:
            flaga = False
        else:
            lis.append(q)
            p = q

    return lis


def otoczkaII(zbior):
    lis =[]
    p = (inf, inf)
    for point in zbior:
        if point[0] < p[0]:
            p = point
        elif point[0] == p[0]:
            if point[1] < p[1]:
                p = point
    lis.append(p)
    copyP = p

    flaga = True
    while flaga:
        if zbior.index(p)+1 >= len(zbior):
            q = zbior[0]
        else:
            q = zbior[zbior.index(p)+1]

        for r in zbior:
            if r != p and r != q:
                ans = check_skretp(p, q, r)
                ans2 = check_skretw(p, r, q)
                if ans:
                    q = r

                if ans2 and dist(p, q) < dist(p, r):
                    q = r

        if q == copyP:
            flaga = False

        else:
            lis.append(q)
            p = q

    return lis

if __name__ == '__main__':
    zbior1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    zbior2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    zbior3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

    # print(otoczkaI(zbior1))
    # print(otoczkaI(zbior2))
    # print()
    # print(otoczkaII(zbior1))
    # print(otoczkaII(zbior2))
    # print()
    print(otoczkaI(zbior3))
    print(otoczkaII(zbior3))

