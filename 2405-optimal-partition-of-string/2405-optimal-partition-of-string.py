class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        We added "#" in the end so that last valid character of the string can receive its judgement properly
        """
    
        count = 0
        path = {"#"}
        s += "#"
        for c in s:
            if c not in path:
                path.add(c)
            else:
                count += 1
                path = {"#"}
                path.add(c)
        
        return count