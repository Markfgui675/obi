n = int(input())
m = int(input())
fig = []
for x in range(m):
    f = int(input())
    if f not in fig:
        fig.append(f)

print(n - len(fig))
