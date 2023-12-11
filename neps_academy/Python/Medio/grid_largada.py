res = []
while True:
    try:
        n = int(input())
        ultrapassagens = 0
        grid_inicial = []
        grid_final = []
        for i in range(n):
            if grid_final.index(grid_final[i]) < grid_inicial.index(grid_final[i]):
                ultrapassagens+= grid_inicial.index(grid_final[i])-grid_final.index(grid_final[i])
    except EOFError:
        break