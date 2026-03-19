class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mod_map = {0: -1}
        running_sum = 0
        
        for i, num in enumerate(nums):
            running_sum += num
            if k != 0:
                running_sum %= k
            
            if running_sum in mod_map:
                if i - mod_map[running_sum] >= 2:
                    return True
            else:
                mod_map[running_sum] = i
        
        return False
            