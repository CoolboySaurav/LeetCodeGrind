class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        op=["+","-","*","/"]
        for t in tokens:
            if t.isdigit() or (t[0] == '-' and t[1:].isdigit()):
                stack.append(int(t))
            elif t=="+":
                a=stack.pop()
                b=stack.pop()
                stack.append(a+b)
            elif t=="-":
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif t=="*":
                a=stack.pop()
                b=stack.pop()
                stack.append(a*b)
            elif t=="/":
                a=stack.pop()
                b=stack.pop()
                if a<0 and b>0:
                    d=abs(b)//abs(a)
                    d=-d
                elif a>0 and b<0:
                    d=abs(b)//abs(a)
                    d=-d
                else:
                    d=b//a
                stack.append(d)
        return stack.pop()