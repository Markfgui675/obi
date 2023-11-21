nums = 0
for i in range(3):
    x = int(input())
    if x%2==0 or str(x)[-1] == '5':
        nums+=1
print(nums)