def horner(wsps, x):
    result = wsps[0]
    for wsps in wsps[1:]:
        result = result * x + wpss
    return result


st_w = int(input("Podaj stopień wielomianu: "))


wsp = []
for i in range(st_w, -1, -1):
    wsp_input = int(input(f"Podaj współczynnik stojący przy potędze {i}: "))
    wsp.append(wsp_input)


x_value = int(input("Podaj argument: "))


result = horner(wsp, x_value)

print(f"W({x_value}) = {result}")
