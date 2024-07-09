class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        result = []

        for i, c in enumerate(s):
            if c == "(":
                result.append("")
                stack.append(i)
            elif c == ")":
                if stack:
                    result[stack.pop()] = "("
                    result.append(c)
                else:
                    result.append("")
            else:
                result.append(c)
        return "".join(result)
        
        
        
        
        stack=[]
        ch=list(s)
        for i in range(len(ch)):
            if ch[i]=="(":
                stack.append(i)
            elif ch[i]==")":
                if stack:
                    stack.pop()
                else:
                    ch[i]=''
        for i in stack:
            ch[i]=''
        return ''.join(ch)     
        