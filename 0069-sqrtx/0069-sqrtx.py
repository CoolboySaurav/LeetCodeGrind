class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        
        l = 1
        r = x // 2
        ans = 0
        
        while l <= r:
            mid = (l + r) // 2
            
            if mid*mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans