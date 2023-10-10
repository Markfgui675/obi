r_copas = []
r_espadas = []
r_ouros = []
r_paus = []

cartas = str(input(''))

intervalo = 0
antigo_intervalo = 0
carta = ''
for c in range(len(cartas)+1):
    if intervalo%3==0 and intervalo!=0:
        carta = cartas[antigo_intervalo:intervalo]
        if carta[-1] == 'C':
            if carta in r_copas:
                r_copas.clear()
                r_copas.append('erro')
            else:
                r_copas.append(carta)
        elif carta[-1] == 'E':
            if carta in r_espadas:
                r_espadas.clear()
                r_espadas.append('erro')
            else:
                r_espadas.append(carta)
        elif carta[-1] == 'U':
            if carta in r_ouros:
                r_ouros.clear()
                r_ouros.append('erro')
            else:
                r_ouros.append(carta)
        else:
            if carta in r_paus:
                r_paus.clear()
                r_paus.append('erro')
            else:
                r_paus.append(carta)
        antigo_intervalo = intervalo
    intervalo+=1

def verifica_erro(lista):
    if 'erro' in lista:
        return 'erro'
    else:
        return 13-len(lista)

print(verifica_erro(r_copas))
print(verifica_erro(r_espadas))
print(verifica_erro(r_ouros))
print(verifica_erro(r_paus))
