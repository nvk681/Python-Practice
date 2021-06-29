def maxSubArray(nums):
        index = 0 
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        while index < len(nums) and nums[index] <= 0:
            index += 1
        if index == len(nums):
            return max(nums)
        max1 = nums[index]
        current_max = max1
        index += 1
        while index < len(nums):
            if nums[index] >= 0:
                current_max += nums[index]
            else: 
                if current_max > max1:
                    max1 = current_max
                if nums[index]+current_max <= 0:
                    current_max = 0
                    while index < len(nums) and nums[index] <= 0:
                        index += 1
                    if index == len(nums)-1 and nums[index] < 0:
                        return max1
                    index -= 1
                else:
                    current_max += nums[index]
            index += 1
        if max1 < current_max:
            max1 = current_max
        return max1

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))
print(maxSubArray([-1,-2,-3,-4]))