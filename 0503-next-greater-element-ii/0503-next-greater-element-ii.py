class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]
        n=len(nums)
        res=[-1]*n
#Min stack implementation
        for i in range(2*n-1,-1,-1):
            if stack and nums[i%n]>=stack[-1]:
                while stack and nums[i%n]>=stack[-1]:
                    stack.pop()
            if i<n:
                if stack and nums[i]<stack[-1]:   
                    res[i]=stack[-1]
            stack.append(nums[i%n])
        return res