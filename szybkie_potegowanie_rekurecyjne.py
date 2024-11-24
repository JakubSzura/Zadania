def potegowanie_rekurencyjne(baza, wykladnik):
    
    if wykladnik == 0:
        return 1
    else:
        
        mniejszy_wynik = potegowanie_rekurencyjne(baza, wykladnik - 1)
        
        wynik = baza * mniejszy_wynik
        return wynik

baza = int(input("Podaj baze: "))
wykladnik = int(input("Podaj wykladnik: "))
wynik = potegowanie_rekurencyjne(baza, wykladnik)

print(f"{baza} do potęgi {wykladnik} wynosi: {wynik}")
