def canJump(nums) -> bool:
        if len(nums) <= 1:
            return True
        max = nums[0]
        if max == 0:
            return False
        index = 1
        limit = len(nums)-1
        if index == limit or max >= limit:
            return True
        while index <= max and index <= limit:
            if index+nums[index] >= limit:
                return True
            else: 
                if index == limit:
                    return False
                if max < index+nums[index]:
                    max = index+nums[index]
                index += 1
        return False

# print(canJump([2,3,1,1,4]))
# print(canJump([3,2,1,0,4]))
print(canJump([1,2,3]))