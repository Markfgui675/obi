h, p, f, d = map(int, input().split())
correto = True
if d == -1:
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
        for i in range(f, h-1, -1):
            if i == p:
                correto = False
                break
if d == 1:
    for i in range(f, (16+h)):
        if i == p:
            correto = False
            break
print('S' if correto else 'N')
