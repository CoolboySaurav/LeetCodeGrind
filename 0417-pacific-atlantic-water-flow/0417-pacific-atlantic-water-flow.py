class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        R=len(heights)
        C=len(heights[0])
        pac=set()
        atl=set()
        
        def dfs(i,j,visit,prevH):
            if (i,j) in visit or i<0 or j<0 or i==R or j==C or heights[i][j]<prevH:
                return 
            visit.add((i,j))
            dfs(i+1,j,visit,heights[i][j])
            dfs(i-1,j,visit,heights[i][j])
            dfs(i,j+1,visit,heights[i][j])
            dfs(i,j-1,visit,heights[i][j])

        for c in  range(C):
            dfs(0,c,pac,heights[0][c])
            dfs(R-1,c,atl,heights[R-1][c])
        
        for r in range(R):
            dfs(r,0,pac,heights[r][0])
            dfs(r,C-1,atl,heights[r][C-1])
        
        res=[]
        for i in range(R):
            for j in range(C):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        
        return res