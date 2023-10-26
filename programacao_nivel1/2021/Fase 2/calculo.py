s = int(input())
a = int(input())
b = int(input())

qtd_soma = 0

for x in range(a,b+1):
    qtd_nums = len(str(x))
    num = str(x)
    nums = []
    for q in range(qtd_nums):
        nums.append(int(num[q]))
    if sum(nums)==s:
        qtd_soma+=1
print(qtd_soma)