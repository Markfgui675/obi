adalberto = 0
bernadete = 0
r_a = 0
r_b = 0

cartas = [4,5,6,7,12,11,13,1,2,3]

cartas_a = []
cartas_b = []

n = int(input())

for i in range(n):
    nums = list(map(int, input().split()))
    a = nums[:3]
    b = nums[3:6]
    cartas_a = [cartas.index(a[0]), cartas.index(a[1]), cartas.index(a[2])]
    cartas_b = [cartas.index(b[0]), cartas.index(b[1]), cartas.index(b[2])]
    if max(cartas_a) > max(cartas_b):
        adalberto+=1
    elif max(cartas_a) < max(cartas_b):
        bernadete+=1
    else:
        adalberto+=1
    cartas_a.clear()
    cartas_b.clear()

print(adalberto, bernadete)
