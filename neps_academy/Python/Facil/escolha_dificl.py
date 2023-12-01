a,b,c = map(int, input().split())
aa,bb,cc = map(int, input().split())

nao_atendidos = 0

if aa > a:
    nao_atendidos+=aa-a
if bb > b:
    nao_atendidos+=bb-b
if cc > c:
    nao_atendidos+=cc-c

print(nao_atendidos)
