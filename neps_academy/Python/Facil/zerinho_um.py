ds = input().split(' ')
dedos = [int(x) for x in ds]
zero = 0
um = 0
for d in dedos:
    if d == 0:
        zero+=1
    if d == 1:
        um+=1 
if um == 1:
    for o in range(len(dedos)):
        if dedos[o] == 1:
            if o == 0:
                print('A')
            elif o == 1:
                print('B')
            else:
                print('C')
elif zero == 1:
    for o in range(len(dedos)):
        if dedos[o] == 0:
            if o == 0:
                print('A')
            elif o == 1:
                print('B')
            else:
                print('C')
else:
    print('*')