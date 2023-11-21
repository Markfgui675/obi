nums = []
ns = []
for n in range(3):
    x = int(input())
    if x not in ns:
        ns.append(x)
        nums.append([1, x])
    else:
        for nn in nums:
            if nn[1] == x:
                nn[0]+=1
                break

print(sorted(nums)[0][1])
