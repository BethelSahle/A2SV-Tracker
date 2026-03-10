class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}
        operations = 0

        for num in nums:
            target = k - num
            if target in count and count[target] > 0:
                operations += 1
                count[target] -= 1
            else:
                count[num] = count.get(num, 0) + 1

        return operations