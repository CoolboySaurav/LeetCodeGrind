class Solution(object):
    def dailyTemperatures(self, temp):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0]*len(temp)
        stack = []
        
        for i in xrange(len(temp)-1, -1,-1):
            if not stack or temp[stack[-1]] > temp[i]:
                val = i
                if stack:
                    val = stack[-1]
                stack.append(i)
                res[i] = val - i
            
            else:
                while stack and temp[stack[-1]] <= temp[i]:
                    stack.pop()
                val = i
                if stack:
                    val = stack[-1]
                stack.append(i)
                res[i] = val - i
        
        return res
        
        
        
        
        
        # res=[0]*len(temperatures)
        # stack=[]
        # stack.append(len(temperatures)-1)
        # for i in range(len(temperatures)-2,-1,-1):
        #     if temperatures[i]<temperatures[stack[-1]]:
        #         res[i]=stack[-1]-i
        #         stack.append(i)
        #     elif stack and temperatures[i]>=temperatures[stack[-1]]:
        #         while stack:
        #             stack.pop()
        #             if stack and temperatures[i]<temperatures[stack[-1]]:
        #                 res[i]=stack[-1]-i
        #                 stack.append(i)
        #                 break
        #         if not stack:
        #             stack.append(i)
        #             res[i]=stack[-1]-i
        # return res