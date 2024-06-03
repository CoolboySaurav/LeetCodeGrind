class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """   
        
        def area(a,b,i,j):
            l=j-i
            h=min(a,b)
            return l*h
        i,j=0,(len(height)-1)
        vol=0
        while i<j:
            a,b=height[i],height[j]
            vol=max(vol,area(a,b,i,j))
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1
        return vol
