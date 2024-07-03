class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
            
        
        total = 0
        bit = 1
        
        for i in xrange(1,len(s)):
            diff = abs(ord(s[i]) - ord(s[i-1]))
            total += diff
        
        return total        