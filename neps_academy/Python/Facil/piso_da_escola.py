l = int(input())
c = int(input())

area_total = l*c

#calcula quantidade de pisos do tipo 2
pisos2 = (2*(l-1))+(2*(c-1))

#calcula quantidade de pisos do tipo 1
p1 = (area_total-0.5)-(pisos2*0.25)
pisos1 = p1/0.5

print(int(pisos1))
print(pisos2)
