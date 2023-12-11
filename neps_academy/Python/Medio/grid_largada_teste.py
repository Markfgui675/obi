n = int(input())
ultrapassagens = 0
grid_inicial = list(map(int, input().split()))
grid_final = list(map(int, input().split()))
for i in range(n):
    if grid_final.index(grid_final[i]) < grid_inicial.index(grid_final[i]):
        ultrapassagens+= grid_inicial.index(grid_final[i])-grid_final.index(grid_final[i])
print(ultrapassagens)
