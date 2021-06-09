def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1

def searchRange(nums, target):
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        index = binary_search(nums, 0, len(nums)-1, target)
        if index == -1:
            return [-1, -1]
        temp = index
        if temp != 0:
            while temp >= 0 and nums[temp] == target:
                # if temp == 0:
                #     break
                temp -= 1
        else: 
            temp -= 1
        max_temp = index
        while max_temp < len(nums) and nums[max_temp] == target:
            max_temp += 1
        if max_temp == len(nums)-1 and nums[len(nums)-1] == target:
            max_temp += 1
        return [temp+1, max_temp-1]

print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 6))
print(searchRange([2,2], 2))
print(searchRange([5,7,7,8,8,10], 5))
print(searchRange([1,1,2], 1))