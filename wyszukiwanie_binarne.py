
def wyszukiwanie (lista, szukana, l, p):
    sr = (l+p) / 2
    while l <= p:
        if lista[round(sr)] == szukana:
            return round(sr)
        if lista[round(sr)] > szukana:
            p = sr - 1
        else:
            l = sr + 1
        sr = (l + p) / 2
    return -1



lista = [1, 2, 5, 8, 9, 11, 15, 20]

l = 0
p = 7
odp = 0


szukana = int(input("Pojdaj liczbe ktora chcesz znajlezc: "))

if wyszukiwanie(lista, szukana, l, p) == -1:
    print('nie ma liczby')
else:
    print(" Liczba " + str(szukana) + " wystepuje w zbiorze w komorce o indeksie: " +  str(wyszukiwanie(lista,szukana,l,p)))


         
