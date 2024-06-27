class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        # Stack solution
        
        openBracket = []
        star = []
        
        for i in xrange(len(s)):
            if s[i] == "(":
                openBracket.append(i)
            elif s[i] == "*":
                star.append(i)
            else:
                if openBracket:
                    openBracket.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while openBracket:
            if not star:
                return False
            elif openBracket and star:
                if openBracket[-1] < star[-1]:
                    openBracket.pop()
                    star.pop()
                else:
                    return False
                
        
        return  True
        