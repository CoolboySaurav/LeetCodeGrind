class Solution(object):
    def removeKdigits(self, num, k):
        """
        If digits are in increasing order for example 1234567 then we would like to pop from right side
        If the digits are in decreasing order for example 7654321 then we would like to pop from left side
        If we use Monotonic stack with almost increasing pattern, for the increasing pattern of the digits, we will ensure poping
        from right side and for the decreasing pattern, we will again ensure poping from the left side
        """
        
        stack = []
        
        for i in num:
            
            while stack and i < stack[-1] and k > 0:
                stack.pop()
                k -= 1
                
            stack.append(i)
            
        while k > 0:
            stack.pop()
            k -= 1
        
        
        result =  ''.join(stack).lstrip('0')
        
        return result if result else '0'