nums1 = [1,2,3,4,5,6,7]
nums2 = [8,9,10,11,12,13]

intervalo1 = nums1[1:5]
intervalo2 = nums2[1:5]

nums1[1:5] = intervalo2
nums2[1:5] = intervalo1

print(nums1)
print(nums2)
