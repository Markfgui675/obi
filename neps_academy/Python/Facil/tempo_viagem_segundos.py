d1 = int(input())
h1 = int(input())
m1 = int(input())
d2 = int(input())
h2 = int(input())
m2 = int(input())

segundos_d1 = 86400*d1
segundos_d2 = 86400*d2
segundos_h1 = 3600*h1
segundos_h2 = 3600*h2
segundos_m1 = 60*m1
segundos_m2 = 60*m2

ida = segundos_d1+segundos_h1+segundos_m1
chegada = segundos_d2+segundos_h2+segundos_m2

print(chegada-ida)
