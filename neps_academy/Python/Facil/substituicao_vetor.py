nums = []
for i in range(10):
    nums.append(int(input()))

menor = min(nums)
new_nums = []
ocorrencias = []

for p in range(len(nums)):
    if nums[p] == menor:
        ocorrencias.append(p)
        new_nums.append(-1)
    else:
        new_nums.append(nums[p])

print(f'Menor: {menor}')
print(f'Ocorrencias: ', end='')
for o in ocorrencias:
    print(o, end=' ')
print()
for k in new_nums:
    print(k, end=' ')
