class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        r = 0
        
        while r < len(s):
            if not stack or s[r] != stack[-1][0]:
                stack.append([s[r],1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            r += 1
        
        res = ""
        while stack:
            char, cnt = stack.pop()
            res += char*cnt
        
        return res[::-1]