class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        num1idx = {n:i for i,n in enumerate(nums1)}
        res = [-1]*len(nums1)
        stack = []
        
        for i in xrange(len(nums2)-1, -1,-1):
            curr = nums2[i]
            
            while stack and stack[-1] <= curr:
                stack.pop()
            if curr in num1idx:
                if stack:
                    res[num1idx[curr]] = stack[-1]
                else:
                    res[num1idx[curr]] = -1
            
            stack.append(curr)
        
        return res