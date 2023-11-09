n = int(input())
nums = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
for x in range(n):
    y = input()
    for k in y:
        for c in nums:
            if int(k) == c[0]:
                c[1]+=1
                break
        
for p in nums:
    print(f'{p[0]} - {p[1]}')
