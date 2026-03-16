class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k):
            left = 0
            count = 0
            odd = 0
            
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd += 1
                
                while odd > k:
                    if nums[left] % 2 == 1:
                        odd -= 1
                    left += 1
                
                count += right - left + 1
            
            return count
        
        return atMost(k) - atMost(k - 1)