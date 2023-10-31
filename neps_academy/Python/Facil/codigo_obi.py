n = int(input())
nums = input().split(' ')
cens = 0
for pos in range(n):
    if pos+3<=n:
        r = nums[pos:pos+3]
        res = ''
        for i in r:
            res+=i
        if res=='100':
            cens+=1
print(cens)