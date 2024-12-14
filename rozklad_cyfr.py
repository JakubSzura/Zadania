def rozklad_na_czynniki_pierwsze(n):
    czynniki = []
    dzielnik = 2
    while dzielnik * dzielnik <= n:
        while n % dzielnik == 0:
            czynniki.append(dzielnik)
            n //= dzielnik
        dzielnik += 1
    if n > 1:
        czynniki.append(n)
    return czynniki

# Przykład użycia
liczba = int(input("Podaj liczbe: "))
print(f"Czynniki pierwsze liczby {liczba}: {rozklad_na_czynniki_pierwsze(liczba)}")