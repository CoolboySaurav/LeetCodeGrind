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
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stack=[]
        # # end=[")","}","]"]
        # # start=["(","[","{"]
        # parent={"(":")","[":"]","{":"}"}
        # for par in s:
        #     if par not in parent.values():
        #         stack.append(par)
        #     else:
        #         if stack:
        #             val=stack.pop()
        #             if par==parent[val]:
        #                 continue
        #             else:
        #                 return False
        #         else:
        #             return False
        # if stack:
        #     return False
        # else:
        #     return True
                
                
            