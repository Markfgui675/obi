a, b = map(int, input().split())

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

mdc_a = mdc(a)
mdc_b = mdc(b)

print(mdc_a)
print(mdc_b)
if mdc_a != None and mdc_b != None:
    divisor_comum = mdc_a.intersection(mdc_b)
else:
    print('São irredutíveis')

