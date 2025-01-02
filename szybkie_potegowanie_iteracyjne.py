def szybkie_potegowanie_iteracyjne(a, b, m):
    wynik = 1
    podstawa = a % m
    while b > 0:
        if b % 2 == 1: 
            wynik = (wynik * podstawa) % m
        podstawa = (podstawa * podstawa) % m
        b //= 2
    return wynik
