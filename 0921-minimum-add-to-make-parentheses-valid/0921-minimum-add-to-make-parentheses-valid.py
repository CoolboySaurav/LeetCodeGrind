class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        openCount = closeCount = 0
        
        for i in  s:
            if i == "(":
                openCount += 1
            else:
                if openCount > 0:
                    openCount -= 1
                else:
                    closeCount += 1
        
        return openCount + closeCount