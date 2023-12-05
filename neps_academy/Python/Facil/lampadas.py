ia, ib, fa, fb = map(int, input().split())

ia = True if ia == 1 else False
ib = True if ib == 1 else False
fa = True if fa == 1 else False
fb = True if fb == 1 else False

movimentos = 0

if (ia == ib == fa == fb) or (ia == fa and ib == fb):
    print(movimentos)
else:
    while True:
        if ia == ib and fa == fb:
            ia = not ia
            ib = not ib
            movimentos+=1
        elif ia != fa and ib == fb:
            ia = not ia
            movimentos+=1
        else:
            ia = not ia
            ib = not ib
            movimentos+=1
        
        if ia == fa and ib == fb:
            break

    print(movimentos)
