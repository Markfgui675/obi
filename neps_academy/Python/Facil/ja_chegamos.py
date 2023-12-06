res = []
nums = list(map(int, input().split()))
list_aux = nums[:]
for i in range(5):
    nums.insert(i, 0)
    dists = []
    for ii in range(len(nums)):
        if i == 0:
            dists.append(sum(nums[:ii+1]))
        else:
            pos_0 = nums.index(0)
            if ii < pos_0:
                dists.append(sum(nums[ii:pos_0+1]))
            elif ii == pos_0:
                dists.append(0)
            else:
                dists.append(sum(nums[pos_0:ii+1]))
    res.append(dists[:])
    dists.clear()
    nums.remove(0)

for r in res:
    for rr in r:
        print(rr, end=' ')
    print()
