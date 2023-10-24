c = int(input())
k = input().split(' ')
lajotas = [int(x) for x in k]
pulos = 0
ultima = len(lajotas)-1
pos_atual = 0
def pular(x):

    def verifica():
        global pulos
        if x+1 <= ultima:
            if lajotas[x+1] == 1:
                pulos+=1
                return x+1
            else:
                return -1
    
    global pulos, pos_atual
    if x+2 <= ultima:
        if lajotas[x+2] == 1:
            pulos+=1
            pos_atual = x+2
        else:
            pos_atual = verifica()
    elif x+1 <= ultima:
        if lajotas[x+1] == 1:
            pulos+=1
            pos_atual= x+1
        else:
            pos_atual = x
    else:
        pos_atual = -1

while pos_atual < ultima:
    pular(pos_atual)
    if pos_atual == -1:
        pulos = pos_atual
        break
            
print(pulos)
