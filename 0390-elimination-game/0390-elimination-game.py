class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        observation:
         for odd n:
            going left or right -> head increments
         for even n:
            going left to right -> head increment
            going right to left -> head constant
        """
        
        
        
        
        if n == 1:
            return 1
        
        head = 1
        step = 1
        leftToRight = True
        
        while n > 1:
            if n % 2:
                head += step
            else:
                if leftToRight:
                    head += step
            step *= 2
            n //= 2
            leftToRight = not leftToRight
        
        return head