infectados_primarios = []
total = []
n, c = map(int, input().split())
for i in range(c):
    lista = list(map(int, input().split()))
    f = lista[0]
    lista = lista[2:][:]
    if i == 0:
        infectados_primarios.append(f)
        total.append(lista)
    else:
        if f != total[-1][-1]:
            infectados_primarios.append(f)
            total.append(lista)
for r in sorted(infectados_primarios):
    print(r)
