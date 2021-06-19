def jump(nums) -> int:
        if len(nums) == 1:
            return 0
        new_list = list()
        for index in range(len(nums)):
            new_list.append(index+nums[index])
        total = 0
        start = 0
        end = len(nums)-1
        while start != end:
            for index in range(start, end+1):
                if new_list[index] >= end:
                    total += 1
                    end = index
                    break
        return total

print(jump([2,3,1,1,4]))
print(jump([2,3,0,1,4]))
print(jump([2,1]))
print(jump([1,1,1,1]))