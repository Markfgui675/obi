palavra = input()
palavra_decodificada = ''

for p in range(len(palavra)):
    if p >= 1:
        if p < len(palavra)-1:
            if palavra[p] == ' ':
                palavra_decodificada+=palavra[p]
            elif (palavra[p+1] == ' ' or palavra[p+1] == 'p') and (palavra[p-1] == ' ' or palavra[p-1] == 'p'):
                if palavra[p] == 'p' and palavra_decodificada[-1] != 'p':
                    palavra_decodificada += palavra[p]
                elif palavra[p] != 'p':
                    palavra_decodificada+=palavra[p]
        else:
            palavra_decodificada+=palavra[p]

print(palavra_decodificada)        
