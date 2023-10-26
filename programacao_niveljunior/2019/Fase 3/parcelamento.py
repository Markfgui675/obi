v = int(input())
p = int(input())

if v%p==0:
    for parcelas in range(p):
        print(int(v/p))
else:
    parcelas_iniciais = v%p
    parcelas_finais = p-parcelas_iniciais
    pi = 0
    pf = 0
    for k in range(p, 0, -1):
        calculo = v - k*parcelas_iniciais
        if calculo%parcelas_finais==0:
            pi = (v-calculo)/parcelas_iniciais
            pf = calculo/parcelas_finais
            break

    for p_i in range(parcelas_iniciais-1):
        print(int(pi))

    for p_f in range(parcelas_finais):
        print(int(pf))
