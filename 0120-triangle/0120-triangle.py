class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        # Recursion
        # def travel(i,j):
        #     if i==n-1:
        #         return triangle[i][j]
        #     down=triangle[i][j]+travel(i+1,j)
        #     diagonal=triangle[i][j]+travel(i+1,j+1)
        #     return min(down,diagonal)
        # return travel(0,0)

        #Memoization
        # dp=[[-1]*len(triangle[i]) for i in range(n)]
        # def travel(i,j):
        #     if i==n-1:
        #         return triangle[i][j]
        #     if dp[i][j]!=-1: 
        #         return dp[i][j]
        #     down=triangle[i][j]+travel(i+1,j)
        #     diagonal=triangle[i][j]+travel(i+1,j+1)
        #     dp[i][j]=min(down,diagonal)
        #     return dp[i][j]
        # return travel(0,0)

        #Tabulation always the opposite of memoization in terms of execution ( flow of code)
        # dp=[[0]*len(triangle[i]) for i in range(n)]
        # for i in range(n):
        #     dp[n-1][i]=triangle[n-1][i]

        # for i in range(n-2,-1,-1):
        #     for j in range(i,-1,-1):
        #         down=dp[i+1][j]
        #         diagonal=dp[i+1][j+1]
        #         dp[i][j]=triangle[i][j]+min(down,diagonal)
        # return dp[0][0]     

        #Space Optimization
        for i in xrange(n-2,-1,-1):
            for j in xrange(i,-1,-1):
                triangle[i][j]+=min(triangle[i+1][j+1],triangle[i+1][j])
        
        return triangle[0][0]
