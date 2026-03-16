class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        curr_sum = 0
        seen = set()
        max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            curr_sum += nums[right]

            if right - left + 1 > k:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum