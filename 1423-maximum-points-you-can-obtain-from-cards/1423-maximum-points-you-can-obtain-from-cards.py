class Solution(object):
    def maxScore(self, c, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if len(c) == 1:
            return c[0]    
        
        lsum = rsum = 0

        for i in xrange(k):
            lsum += c[i]
        
        tot = lsum
        l = k - 1
        r = len(c) - 1
        while k > 0 :
            lsum -= c[l]
            l -= 1
            rsum += c[r]
            r -= 1
            tot = max(tot,lsum + rsum)
            k -= 1
        
        return tot