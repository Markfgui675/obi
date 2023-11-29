a = int(input())
b = int(input())
c = int(input())
h = int(input())
l = int(input())

areas = [[a, b], [a, c], [b, c]]

tem_como = False

for ar in areas:
    if (ar[0] <= h and ar[1] <= l) or (ar[0] <= l and ar[1] <= h):
        tem_como = True
        break

print('S' if tem_como else 'N')
