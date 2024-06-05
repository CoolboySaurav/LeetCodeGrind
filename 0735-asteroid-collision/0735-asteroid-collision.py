class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        res=[]
        for i in asteroids:
            if not stack and i<0:
                res.append(i)
            elif i>0:
                stack.append(i)
            elif stack and i<0:
                c,e=0,0
                while stack:
                    if abs(stack[-1])>abs(i):
                        break
                    elif abs(stack[-1])<abs(i):
                        c+=1
                        stack.pop()
                    else:
                        stack.pop()
                        e+=1
                        break
                if c!=0 and not stack and e==0:
                    res.append(i)
        if stack:
            for i in stack:
                res.append(i)
        return res