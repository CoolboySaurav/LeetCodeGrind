class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Recursive solution a Top-Down Approach is used
        # visit=set()
        # count=[0]
        # def travel(i,j):
        #     if i==j==0:
        #         return 1
        #     if i<0 or j<0 or (i,j) in visit:
        #         return 0
        #     visit.add((i,j))
        #     up=travel(i-1,j)
        #     left=travel(i,j-1)
        #     visit.remove((i,j))
        #     return up+left
        # return travel(m-1,n-1)

        # Memoization Approach to reduce the time complexity
        # dp=[[-1]*n for _ in range(m)]
     
        # def travel(i,j):
        #     if i==j==0:
        #         return 1
        #     if i<0 or j<0:
        #         return 0
            
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     up=travel(i-1,j)
        #     left=travel(i,j-1)
            
        #     dp[i][j]=up+left
        #     return dp[i][j]
        # return travel(m-1,n-1)
        
        # Tabulation Approach to reduce the space complexity (eliminate the stack space)

        # dp=[[0]*n for _ in range(m)]
        # dp[0][0]=1
        # for i in range(m):
        #     for j in range(n):
        #         up=left=0
        #         if i==j==0:
        #             continue
        #         else:
        #             if i>0:
        #                 up=dp[i-1][j]
        #             if j>0:
        #                 left=dp[i][j-1]
        #             dp[i][j]=up+left
        # return dp[m-1][n-1]

        # Space Optimization 
        prev=[0]*n

        for i in xrange(m):
            temp=[0]*n
            for j in xrange(n):
                if i==j==0:
                    temp[j]=1
                    continue
                up=left=0
                if i>0:
                    up=prev[j]
                if j>0:
                    left=temp[j-1]
                temp[j]=up+left
            prev=temp
        return prev[n-1]