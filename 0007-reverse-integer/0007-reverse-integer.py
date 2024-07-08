class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        intMin, intMax = -2**31, 2**31 - 1
        temp = abs(x)
        res = 0
        
        while temp != 0:
            
            lastDigit = temp % 10
            res = res*10 + lastDigit
            temp //= 10
        if x < 0:
            res = -res
        
        return res if intMin <= res <= intMax else 0