k = int(input())
ar = list(map(int, input().split()))
remainder_set = set()
pairs = 0

for num in ar:
    complement = (k - num) % k
    if complement in remainder_set:
        pairs += 1

    remainder_set.add(num % k)

print(pairs)
                