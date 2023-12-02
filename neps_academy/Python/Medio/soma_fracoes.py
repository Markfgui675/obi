a, b, c, d = map(int, input().split())
res = []





def mdc(x: int) -> set | None:
    f = x
    divisores_x = set()
    dx = 2
    while dx < f:
        if x%dx==0:
            x = int(x/dx)
            divisores_x.add(dx)
        else:
            dx+=1
    if len(divisores_x) == 0:
        return None
    return divisores_x




def calculo(x: int, y: int) -> 




numerador = 0
denominador = 0
if b == d:
    #processo de divisão (MDC) irredutível
    numerador = a+c
    denominador = b
    if mdc(numerador) != None and mdc(denominador) != None:
        divisor_comum = mdc(numerador).intersection(mdc(denominador))
        for i in divisor_comum:
            dc = i
    else:
        res.append(numerador)
        res.append(denominador)
else:
    ...

for r in res:
    print(r, end=' ')






