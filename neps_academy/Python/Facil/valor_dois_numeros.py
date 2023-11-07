n1 = int(input())
n2 = int(input())

if n1 > n2:
    for i in range(n2, n1+1):
        print(i, end=' ')
elif n1 < n2:
    for i in range(n1, n2+1):
        print(i, end=' ')
else:
    print(n1)
