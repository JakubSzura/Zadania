def horner(coeffs, x):
    result = coeffs[0]
    for coeff in coeffs[1:]:
        result = result * x + coeff
    return result


st_w = int(input("Podaj stopień wielomianu: "))


wsp = []
for i in range(st_w, -1, -1):
    wsp_input = int(input(f"Podaj współczynnik stojący przy potędze {i}: "))
    wsp.append(wsp_input)


x_value = int(input("Podaj argument: "))


result = horner(wsp, x_value)

print(f"W({x_value}) = {result}")