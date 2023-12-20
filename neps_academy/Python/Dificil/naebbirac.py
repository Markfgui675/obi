k, n = map(int, input().split())
nums = list(map(int, input().split()))

ns = []
count_nums = []

for i in nums:
    if i in range(1, k+1) and i not in ns:
        ns.append(i)
        count_nums.append([1, i])
    else:
        for ii in count_nums:
            if ii[1] == i:
                ii[0]+=1
                break
count_nums = sorted(count_nums, reverse=True)

if max(count_nums)[0] - min(count_nums)[0] == 1:
    if count_nums[0][0] == count_nums[1][0]:
        print(f'+{count_nums[-1][1]}')
    elif count_nums[0][0] > count_nums[1][0]:
        print(f'-{count_nums[0][1]}')

elif max(count_nums)[0] - min(count_nums)[0] == 2:
    print(f'-{count_nums[0][1]} +{count_nums[-1][1]}')
else:
    print('*')
