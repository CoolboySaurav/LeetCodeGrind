class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = fast = n
        
        while True:
            slow = self.solve(slow)
            fast = self.solve(self.solve(fast))
            if slow == fast == 1:
                return True
            if slow == fast:
                return False
            
            
    def solve(self, n):
        tot = 0
        while n:
            tot += ((n % 10) ** 2)
            n = n // 10
        return tot