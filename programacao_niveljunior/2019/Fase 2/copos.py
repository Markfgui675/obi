n = int(input())
copo = input()

A, B, C = 0, 0, 0

if copo == 'A':
    A = 1
elif copo == 'B':
    B = 1
else:
    C = 1

for _ in range(int(n)):
    operacao = int(input())

    if operacao == 1:
        A, B = B, A
    elif operacao == 2:
        B, C = C, B
    else:
        A, C = C, A

if A == 1:
    print("A")
elif B == 1:
    print("B")
else:
    print("C")
