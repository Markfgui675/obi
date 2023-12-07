'''
n = int(input())
nums = list(map(int, input().split()))

possiveis = 0
ultimo_maior = nums[-1]

for i in range(n-2, -1, -1):
    if nums[i] == ultimo_maior - 1:
        possiveis+=n-(i+1)
        ultimo_maior = nums[i]

print(possiveis)
'''

def count_inversions(nums):
    if len(nums) <= 1:
        return nums, 0

    meio = len(nums) // 2
    esquerda, inv_esquerda = count_inversions(nums[:meio])
    direita, inv_direita = count_inversions(nums[meio:])
    merged, inv_merger = merge_and_count_split_inversions(esquerda, direita)

    return merged, (inv_esquerda + inv_direita + inv_merger)

def merge_and_count_split_inversions(esquerda, direita):
    merged = []
    i, j, split_inversions = 0, 0, 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            merged.append(esquerda[i])
            i += 1
        else:
            merged.append(direita[j])
            j += 1
            split_inversions += len(esquerda) - i

    merged += esquerda[i:]
    merged += direita[j:]

    return merged, split_inversions

n = int(input())
nums = list(map(int, input().split()))

sorted_nums, inversions = count_inversions(nums)
print(inversions)
print(sorted_nums)
