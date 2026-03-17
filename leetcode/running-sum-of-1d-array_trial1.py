class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []
        total = 0
        for num in nums:
            total += num
            result.append(total)
        return result


        