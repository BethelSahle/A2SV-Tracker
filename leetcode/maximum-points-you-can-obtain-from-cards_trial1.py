class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        
        if k == n:
            return sum(cardPoints)
        
        window = n - k
        total = sum(cardPoints)
        
        curr = sum(cardPoints[:window])
        min_sum = curr
        
        for i in range(window, n):
            curr += cardPoints[i]
            curr -= cardPoints[i - window]
            min_sum = min(min_sum, curr)
        
        return total - min_sum