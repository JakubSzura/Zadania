def f(x):
    return x * (x * (x - 3) + 2) - 6

def polowienie_przedzialow(a, b, epsilon):
    if f(a) == 0.0:
        return a
    if f(b) == 0.0:
        return b
    srodek = (a + b) / 2
    if abs(b - a) <= epsilon:
        return srodek
    if f(a) * f(srodek) < 0:
        return polowienie_przedzialow(a, srodek, epsilon)
    else:
        return polowienie_przedzialow(srodek, b, epsilon)

a = -10
b = 10
epsilon = 0.00001

miejsce_zerowe = polowienie_przedzialow(a, b, epsilon)
print(round(miejsce_zerowe, 5))
