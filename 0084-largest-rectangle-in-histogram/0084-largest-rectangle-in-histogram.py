class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = float('-inf')
        st = []
        
        for i, h in enumerate(heights):
            start = i
            
            while st and st[-1][1] > h:
                maxArea = max(maxArea, (st[-1][1] * (i - st[-1][0])))
                start = st[-1][0]
                st.pop()

            st.append([start, h])
        
        n = len(heights)
        while st:
            maxArea = max(maxArea, (st[-1][1] * (n - st[-1][0])))
            st.pop()
        return maxArea