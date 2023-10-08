n = int(input(''))

def numerosDasMaos(n: int):
    m_esquerda = []
    m_direita = []
    dedo = 'I'
    result_e = ''
    result_d = ''
    if n == 0:
        return f'*\n*'
    elif n <= 5:
        for d in range(n):
            m_esquerda.append(dedo)
        
        for dre in range(n):
            if dre == 0:
                result_e = m_esquerda[dre]
            else:
                result_e += m_esquerda[dre]
        
        return f'{result_e}\n*'
    else:
        dif = n - 5
        for d_e in range(5):
            m_esquerda.append(dedo)
        for d_d in range(dif):
            m_direita.append(dedo)
        
        for dre in range(5):
            if dre == 0:
                result_e = m_esquerda[dre]
            else:
                result_e += m_esquerda[dre]
        
        for drd in range(dif):
            if drd == 0:
                result_d = m_direita[drd]
            else:
                result_d += m_direita[drd]
        
        return f'{result_e}\n{result_d}'
    

print(numerosDasMaos(n))
