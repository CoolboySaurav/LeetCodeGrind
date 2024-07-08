class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        r = 0
        
        while r < len(s):
            if not stack or stack[-1] != s[r]:
                stack.append(s[r])
            else:
                stack.pop()
            r += 1
        
        return "".join(stack)