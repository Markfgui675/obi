m2 = 0
m3 = 0
m4 = 0

n = int(input())
for i in range(n):
    x = int(input())
    if x%4==0:
        m4+=1
    if x%3==0:
        m3+=1
    if x%2==0:
        m2+=1

print(m2)
print(m3)
print(m4)
