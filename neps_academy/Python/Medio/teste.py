f = 7
h = 14
p = 1
correto = True
if h > f:
    for i in range(f, -1, -1):
        if i == p:
            correto = False
            break
    if correto:
        for i in range(15, h-1, -1):
            if i == p:
                correto = False
                break
else:    
    for i in range(f, h, -1):
        print(i)
print('S' if correto else 'N')
