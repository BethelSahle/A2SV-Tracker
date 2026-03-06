class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
    
        if num < 0:
  
            digits = sorted(str(num)[1:], reverse=True)
            return -int("".join(digits))
        
        digits = sorted(str(num))
        
        if digits[0] == '0':
            for i in range(len(digits)):
                if digits[i] != '0':
                    digits[0], digits[i] = digits[i], digits[0]
                    break
                    
        return int("".join(digits))