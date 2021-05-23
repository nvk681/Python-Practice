def removeDuplicates(nums) -> int:
        if len(nums) == 0:
            return []
        index = 0
        while index <= len(nums):
            if index < len(nums)-1 :
                if nums[index] == nums[index+1]:
                    nums.pop(index)
                else:
                    index += 1
            else:
                index += 1
        return nums

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([]))
print(removeDuplicates([1,2,3]))
print(removeDuplicates([12]))