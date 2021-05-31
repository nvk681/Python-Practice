class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        is_not_in_dec = True
        for index in range(0, len(nums)-1):
            if nums[index] < nums[index+1]:
                is_not_in_dec = False
                break
        if is_not_in_dec:
            nums.sort()
            return
        i = len(nums) - 2
        while not (i < 0 or nums[i] < nums[i+1]):
            i -= 1
            if i < 0:
                return False
        j = len(nums) - 1
        while not (nums[j] > nums[i]):
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:]) 

# a = [1,2,3]
# nextPermutation(a)
# print(a)
# a = [3,2,1]
# nextPermutation(a)
# print(a)
# a = [1,1,5]
# nextPermutation(a)
# print(a)
# a = [1]
# nextPermutation(a)
# print(a)
# a = [1,3,2]
# nextPermutation(a)
# print(a)
a = [4,2,0,2,3,2,0]
nextPermutation(a)
print(a)