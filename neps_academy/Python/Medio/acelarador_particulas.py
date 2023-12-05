n = int(input())

pos = 0

for i in range(n-3):
    if pos < 7:
        pos+=1
    else:
        pos = 0

if pos == 1 or pos in range(1, 4):
    print(1)
elif pos == 2 or pos in range(2, 5):
    print(2)
elif pos == 3 or pos in range(3, 6):
    print(3)
