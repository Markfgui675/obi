h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))
compativel = True
for h in range(len(h1)):
    if h1[h] == h2[h]:
        compativel = False
        break
print('Y' if compativel else 'N')
