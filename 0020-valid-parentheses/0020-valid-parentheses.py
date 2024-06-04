class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        
        for i in s:
            if i in  ['(','[','{']:
                stack.append(i)
            else:
                if stack:
                    if brackets[i] == stack[-1]:
                        stack.pop()
                        continue
                    else:
                        return False
                else:
                    return False
        return not stack   
                
            