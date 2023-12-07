n = int(input())
nums = list(map(int, input().split()))

possiveis = 0

for i in range(n):
    for j in range(i+1,n):
        if nums[i]>nums[j]:
            possiveis+=1

print(possiveis)
