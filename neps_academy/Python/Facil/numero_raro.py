n = int(input())
nums = list(map(int, input().split()))
ocorrencias = []
n_ocorrencias = []
for i in nums:
    if i not in n_ocorrencias:
        n_ocorrencias.append(i)
        ocorrencias.append([1, i])
    else:
        for f in ocorrencias:
            if f[1] == i:
                f[0]+=1
print(sorted(ocorrencias)[0][1])
