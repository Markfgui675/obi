n, f = map(int, input().split())

result = abs((f*100/n)-100)

print(f'{result:.2f}%')
