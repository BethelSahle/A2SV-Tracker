class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        count = 0
        max_count = 0

        for i in range(len(s)):
            if s[i] in vowels:
                count += 1

            if i >= k and s[i-k] in vowels:
                count -= 1

            max_count = max(max_count, count)

        return max_count