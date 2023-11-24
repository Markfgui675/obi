n, m = map(int, input().split())
premio_intervalo = list(map(int, input().split()))
premio = list(map(int, input().split()))
ogros = list(map(int, input().split()))
res = []

def search(arr: list[int], x: int): 
    r = 0
    if len(arr) == 1 and x < arr[0]:
        r = 0
    elif len(arr) == 1 and x >= arr[0]:
        r = 1
    else:
        for s in range(len(arr)-1):
            if s == 0:
                if x < arr[s]:
                    r = s
                    break
            if x >= arr[-1]:
                r = -1
                break
            else:
                if x in range(arr[s], arr[s+1]):
                    r = s+1
                    break
    return r


for gg in ogros:
    result = search(premio_intervalo, gg)
    res.append(premio[result])

for r in res: 
    print(r, end=' ')
