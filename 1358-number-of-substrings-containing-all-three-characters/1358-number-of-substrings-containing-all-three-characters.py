class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastSeen = [-1,-1,-1]
        count = 0 

        for i in xrange(len(s)):
            lastSeen[ord(s[i]) - ord('a')] = i 
            count = count + 1 + min(lastSeen[0],lastSeen[1],lastSeen[2])
        
        return count
