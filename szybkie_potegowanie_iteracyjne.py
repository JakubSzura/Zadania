
baza = int(input("Podaj baze: "))     
wykladnik = int(input("Podaj wykladnik: ")) 
wynik = 1     


for _ in range(wykladnik):
    wynik *= baza


print(f"{baza} do potęgi {wykladnik} wynosi: {wynik}")