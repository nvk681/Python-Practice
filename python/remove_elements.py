def removeElement(nums, val):
        if len(nums) == 0:
            return 0
        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1
        return len(nums)

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))
print(removeElement([0,1,2,3],5))
print(removeElement([1,2,2,3,4,2], 2))