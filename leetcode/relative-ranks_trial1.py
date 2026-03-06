class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_scores = sorted(score, reverse=True)
        result = []
        i = 0
        while i < len(score):
            s = score[i]
            rank = sorted_scores.index(s) 
            if rank == 0:
                result.append("Gold Medal")
            elif rank == 1:
                result.append("Silver Medal")
            elif rank == 2:
                result.append("Bronze Medal")
            else:
                result.append(str(rank + 1))
            i += 1
        
        return result