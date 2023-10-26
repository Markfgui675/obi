n = int(input())
coin_position = str(input())
for x in range(n):
    move = int(input())
    if move==1:
        if coin_position == 'A':
            coin_position = 'B'
    elif move==2:
        if coin_position == 'B':
            coin_position = 'C'
    elif move==3:
        if coin_position == 'C':
            coin_position = 'A'

print(coin_position)
