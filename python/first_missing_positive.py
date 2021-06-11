def firstMissingPositive(nums):
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1
        nums.sort()
        current = 1
        nums = [ele for ele in nums if ele > 0]
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1
        for i in range(len(nums)-1):
            if current != nums[i]:
                return 1
            else: 
                while i < len(nums)-1 and (nums[i]+1 == nums[i+1] or nums[i] == nums[i+1]):
                    i += 1
                if i == len(nums)-2 and nums[i]+1 == nums[i+1]:
                    return nums[i+1]+1
                else:
                    return nums[i]+1
        return 1

print(firstMissingPositive([1, 1000]))
print(firstMissingPositive([1, 0]))
print(firstMissingPositive([-1, -2]))
print(firstMissingPositive([1,2,0]))
print(firstMissingPositive([3,4,-1,1]))
print(firstMissingPositive([7,8,9,11,12]))