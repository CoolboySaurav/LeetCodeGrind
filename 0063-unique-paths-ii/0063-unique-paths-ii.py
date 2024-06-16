class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        
        # Memoization Approach to reduce the time complexity to O(m*n)
        # dp=[[-1]*n for _ in range(m)]
     
        # def travel(i,j):
        #     if i==j==0:
        #         return 1
        #     if i<0 or j<0 or obstacleGrid[i][j]==1:
        #         return 0
            
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     up=travel(i-1,j)
        #     left=travel(i,j-1)
            
        #     dp[i][j]=up+left
        #     return dp[i][j]
        # return travel(m-1,n-1)
        
        
        # Tabulation Apporach to reduce the space complexity by eliminating recursion stack space
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                up=left=0
                if i==j==0 or obstacleGrid[i][j]==1:
                    continue
                else:
                    if i>0:
                        up=dp[i-1][j]
                    if j>0:
                        left=dp[i][j-1]
                    dp[i][j]=up+left
        return dp[m-1][n-1]

        # Can do the space optimization as well