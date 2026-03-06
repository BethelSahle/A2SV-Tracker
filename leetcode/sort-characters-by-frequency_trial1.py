class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        max_freq = max(freq.values())

        result = ""
        for f in range(max_freq, 0, -1):
            for ch in freq:
                if freq[ch] == f:
                    result += ch * f

        return result