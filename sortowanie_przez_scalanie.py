def merge(tab, l, m, r):
    lSize = m - l + 1
    rSize = r - m
    tabL = [0] * lSize
    tabR = [0] * rSize

    for x in range(lSize):
        tabL[x] = tab[l + x]
    for y in range(rSize):
        tabR[y] = tab[m + 1 + y]

    indexL = 0
    indexR = 0
    currIndex = l

    while indexL < lSize and indexR < rSize:
        if tabL[indexL] <= tabR[indexR]:
            tab[currIndex] = tabL[indexL]
            indexL += 1
        else:
            tab[currIndex] = tabR[indexR]
            indexR += 1
        currIndex += 1

    while indexL < lSize:
        tab[currIndex] = tabL[indexL]
        indexL += 1
        currIndex += 1

    while indexR < rSize:
        tab[currIndex] = tabR[indexR]
        indexR += 1
        currIndex += 1

def merge_sort(tab, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(tab, l, m)
        merge_sort(tab, m + 1, r)
        merge(tab, l, m, r)

tablica = [38, 27, 43, 3, 9, 82, 10]
merge_sort(tablica, 0, len(tablica) - 1)
print("Posortowana tablica:", tablica)
