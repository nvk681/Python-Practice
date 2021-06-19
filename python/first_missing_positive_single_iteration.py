 def firstMissingPositive(nums):
        n = len(nums)
        for index in range(n):
            item = nums[index]-1
            while 1 <= nums[index] <= n and nums[index] != nums[item]:
                nums[index], nums[item] = nums[item], nums[index]
                item = nums[index]-1
        for index in range(n):
            if index+1 != nums[index]:
                return index+1
        return n+1