class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1:
            return 1
        
        up = down = 1
        result = 1
        
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                up = down + 1
                down = 1
            elif arr[i] < arr[i-1]:
                down = up + 1
                up = 1
            else:
                up = down = 1
            
            result = max(result, up, down)
        
        return result
