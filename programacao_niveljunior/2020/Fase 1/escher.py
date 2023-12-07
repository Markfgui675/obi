n = int(input())
nums = list(map(int, input().split()))

soma = nums[0]+nums[-1]
escher = True

for i in range(1, n+1):
    if nums[i]+nums[n-1+1] != soma:
        escher = False
        break

if escher:
    print('S')
else:
    print('N')
