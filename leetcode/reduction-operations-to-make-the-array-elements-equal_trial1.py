class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        operations= 0
        steps = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                steps += 1
            operations += steps

        return operations