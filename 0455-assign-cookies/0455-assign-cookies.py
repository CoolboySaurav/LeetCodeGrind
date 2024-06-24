class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        l,r=0,0
        count=0
        for l in range(len(g)):
            if r<len(s) and s[r]<g[l]:
                while r<len(s) and s[r]<g[l]:
                    r+=1
                if r==len(s):
                    break
            if r<len(s) and s[r]>=g[l]:
                count+=1          
                r+=1
        return count