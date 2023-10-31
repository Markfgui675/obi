n = int(input())
copos_quebrados = 0
for e in range(n):
    l, c = map(int, input().split())
    if l > c:
        copos_quebrados+=c
print(copos_quebrados)
