class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        left = 0
        pairs = 0
        res = 0
        n = len(nums)

        for right in range(n):
            pairs += freq[nums[right]]
            freq[nums[right]] += 1

            while pairs >= k:
                res += (n - right)

                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1

        return res
            