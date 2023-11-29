n = int(input())

v = 0
if n > 1:
    while n > 1:
        if n%2==0:
            n = n/2
        else:
            n = 3*n + 1
        v+=1
    print(v)
else:
    print(v)
