n = int(input(''))

dicio = {}

for i in range(n):
    e, a, c = str(input('')).split(' ')
    dicio.update({f'{e}':(float(a),float(c))})

estado_mais_vantajoso = []
n_vantojoso = 0
n_mais_vantojoso = 0
percent = 0

for x in dicio.keys():
    percent = (dicio[x][1]*70)/100
    n_vantojoso = dicio[x][0]
    if n_vantojoso <= percent:
        estado_mais_vantajoso.append(x)

if len(estado_mais_vantajoso)==0:
    print('*')
else:
    for e in range(len(estado_mais_vantajoso)):
        print(estado_mais_vantajoso[e])
