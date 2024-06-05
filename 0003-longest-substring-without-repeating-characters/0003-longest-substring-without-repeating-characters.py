class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        char = set()
        l = 0 
        for i in xrange(len(s)):    
            if s[i] in char:
                while s[i] in char:
                    char.remove(s[l])
                    l += 1
            char.add(s[i])
            res = max(res, len(char))
        
        return res
        