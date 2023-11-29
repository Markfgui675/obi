n = int(input())
arr = list(map(int, input().split()))
ids = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
for a in arr:
    ids[a-1][1]+=1
print(sorted(ids, key=lambda x: x[1], reverse=True)[0][0])