class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R=len(grid)
        C=len(grid[0])

        # Recursion 
        
        # def compute(i,j):
        #     if i==j==0:
        #         return grid[i][j]
        #     if i<0 or j<0:
        #         return 1e7
        #     up=grid[i][j]+compute(i-1,j)
        #     left=grid[i][j]+compute(i,j-1)
        #     return min(up,left)
        # return compute(R-1,C-1)

        #Memization
        
        # dp=[[-1]*C for _ in xrange(R)]
        # def compute(i,j):
        #     if i==j==0:
        #         return grid[i][j]
        #     if i<0 or j<0:
        #         return 1e7
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     up=grid[i][j]+compute(i-1,j)
        #     left=grid[i][j]+compute(i,j-1)
        #     dp[i][j]= min(up,left)
        #     return dp[i][j]
        # return compute(R-1,C-1)

        #Tabulation
        
        # dp=[[0]*C for _ in xrange(R)]
        # dp[0][0]=grid[0][0]
        # for i in xrange(R):
        #     for j in xrange(C):
        #         if i==j==0:
        #             continue
        #         up=left=1e7
        #         if i>0:
        #             up=dp[i-1][j]
        #         if j>0:
        #             left=dp[i][j-1]
        #         dp[i][j]=grid[i][j]+min(up,left)
        # return dp[R-1][C-1]

        #Space Optimization
        
        prev=[0]*C
        for i in xrange(R):
            temp=[0]*C
            for j in xrange(C):
                if i==j==0:
                    temp[0]=grid[i][j]
                    continue
                up=left=1e7
                if i>0:
                    up=prev[j]
                if j>0:
                    left=temp[j-1]
                temp[j]=grid[i][j]+min(up,left)
            prev=temp
        return prev[C-1]
