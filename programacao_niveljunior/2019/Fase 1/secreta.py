n = int(input())
ultimo_numero = 0
circulos = 0
for s in range(n):
    x = int(input())    
    if s == 0:
        ultimo_numero = x
        circulos+=1
    else:
        if x != ultimo_numero:
            ultimo_numero = x
            circulos+=1
print(circulos)
