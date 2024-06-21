class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        stack = [] # [ind, height]
        maxArea = 0
        
        for i, h in enumerate(heights):
            start = i
            
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                maxArea = max(maxArea, height*(i - ind))
                start = ind
            stack.append([start, h])
        
        while stack:
            ind, h = stack.pop()
            maxArea = max(maxArea, h*(n-ind))
        
        return maxArea