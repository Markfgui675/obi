
def quota(x, quota_meses):
    acumulado = x
    diferenca = 0
    result = 0
    for k in range(len(quotas_meses)):
        diferenca = acumulado-quota_meses[k]
        acumulado = x + diferenca
    resultado = acumulado
    return resultado


x = int(input(''))
n = int(input(''))
quotas_meses = []
for y in range(n):
    z = int(input())
    quotas_meses.append(z)

resultado = quota(x, quotas_meses)
print(resultado)

