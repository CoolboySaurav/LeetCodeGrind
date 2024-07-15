class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.maxLen = -1
        self.res = set()
        
        self.helper(0, s, "", 0, 0)
        return list(self.res)
    
    def helper(self, ind, s, path, open, close):
        if ind == len(s):
            if open == close:
                if len(path) > self.maxLen:
                    self.maxLen = len(path)
                    self.res = {path}
                elif len(path) == self.maxLen:
                    self.res.add(path)
            return
        
        ch = s[ind]
        
        if ch == "(":
            # Consider the open bracket
            self.helper(ind + 1, s, path + ch, open + 1, close)
            # Don't consider and skip
            self.helper(ind + 1, s, path, open, close)
        elif ch == ")":
            # Don't consider and skip
            self.helper(ind + 1, s, path, open, close)
            # Consider the close bracket
            if open > close:
                self.helper(ind + 1, s, path + ch, open, close + 1)
        else:
            # Add non-parenthesis character to the path
            self.helper(ind + 1, s, path + ch, open, close)

