n = int(input())

v = 0
nums = []
if n > 1:
    while n > 1:
        nums.append(n)
        if n%2==0:
            n = n/2
        else:
            n = 3*n + 1
        v+=1
    print(v)
    print(f'Maior valor: {max(nums)}')
else:
    print(v)
