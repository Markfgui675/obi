data = input().split('/')

if int(data[0]) <= 12 and int(data[1]) <= 12:
    print('either')
elif int(data[0]) > 12 and int(data[1]) <= 31:
    print('EU')
elif int(data[0]) <= 12 and int(data[1]) <= 31:
    print('US')
