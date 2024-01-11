n = int(input())
nums = list(map(int, input().split()))

mais_de_um_pico = False

for i in range(1, len(nums)-1):
    if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
        mais_de_um_pico = True
        break

if mais_de_um_pico:
    print('S')
else:
    print('N')
