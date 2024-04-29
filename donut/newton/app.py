from math import factorial

f = lambda a,b: (factorial(a))/(factorial(b)*factorial(a-b))

# (x+y)³ = x³ + 3x²y + 3xy² + y³

def calc(x:int, c_a = 'x', c_b = 'y') -> list:
    comb_6 = []

    for i in range(x+1):
        if i <= x:
            k = f'{f(x,i)}{c_a}^{x-i}{c_b}^{i}'
            comb_6.append(k)

    return comb_6

print(calc(3))
