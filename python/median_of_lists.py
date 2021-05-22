def findMedianSortedArrays(nums1, nums2) -> float:
    big_list = []
    median = 0
    while len(nums1) != 0 and len(nums2) != 0:
        if nums1[0] < nums2[0]:
            big_list.append(nums1.pop(0))
        else:
            big_list.append(nums2.pop(0))
    if len(nums1) != 0:
        big_list = big_list+nums1
    if len(nums2) != 0:
        big_list = big_list+nums2
    mid = (len(big_list)//2)
    if len(big_list)%2 == 0:
        median = (big_list[mid]+big_list[mid-1])/2
    else:
        median = big_list[mid]
    return median

print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,2], [3,4]))
print(findMedianSortedArrays([0,0], [0,0]))
print(findMedianSortedArrays([], [1]))
print(findMedianSortedArrays([2], []))