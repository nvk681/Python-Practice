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

def search(nums, target):
        if len(nums) == 0:
            return -1
        min = None
        max = None
        second = None
        for index in range(len(nums)-1):
            if nums[index] > nums[index+1]:
                min = nums[index+1]
                max = nums[index]
                second = index+1
        if min is None:
            return binary_search(nums, 0, len(nums)-1, target)
        if target < min or target > max :
            return -1
        if target <= nums[second-1] and target >= nums[0]:
            return binary_search(nums, 0, second-1, target)
        else:
            return binary_search(nums, second, len(nums)-1, target)

print(4 == search([4,5,6,7,0,1,2], 0))
print(-1 == search([4,5,6,7,0,1,2], 3))
print(-1 == search([1], 0))
print(-1 == search([], 5))
print(4 == search([1,2,3,4,5], 5))
print(1 == search([3,1], 1))
print(search([3,1], 3))