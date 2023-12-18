s = int(input())
a = int(input())
b = int(input())

preco = 250

if s <= a:
    print(preco)
else:
    ss = a
    while ss < s:
        preco+=100
        ss+=b
    print(preco)
