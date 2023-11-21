n = int(input())
nums = []
for i in range(3):
    nums.append(int(input()))

soma = 0
q = 0
for i in sorted(nums):
    if soma + i < n:
        soma+=i
        q+=1

print(q)
