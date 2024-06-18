class Solution(object):
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(p)
        #Recursive approach
        # def find(i,b):
              # If we reach n that means we cant do much since no price listed hence return 0
        #     if i == n:
        #         return 0
        #     if b==0:
        #         # If we buy that means we are giving away money hence profit will be -p[i]
        #         profit = max((-p[i]+find(i+1,1)), find(i+1,0))
        #     else:
        #         # If we sell that means we are getting money hence profit will be p[i]
        #         profit = max((p[i]+ find(i+1,0),find(i+1,1)))
        #     return profit    
        # return find(0,0)

        #Memoization
        # dp=[[-1,-1] for _ in xrange(n)]
        # def find(i,b):
        #     if i == n:
        #         return 0
        #     if dp[i][b]!=-1:
        #         return dp[i][b]
        #     if b==0:
        #         # If we buy that means we are giving away money hence profit will be -p[i]
        #         profit = max((-p[i]+find(i+1,1)), find(i+1,0))
        #     else:
        #         # If we sell that means we are getting money hence profit will be p[i]
        #         profit = max((p[i]+ find(i+1,0),find(i+1,1)))
        #     dp[i][b] = profit
        #     return dp[i][b]    
        # return find(0,0)

        # Tabulation
        # dp = [[0,0] for _ in xrange(n+1)]

        # for i in xrange(n-1,-1,-1):
        #     dp[i][0] = max((-p[i]+ dp[i+1][1]), dp[i+1][0])
        #     dp[i][1] = max(p[i]+dp[i+1][0],dp[i+1][1])
        
        # return dp[0][0]

        # Space Optimization

        prev = [0,0]
        for i in xrange(n-1,-1,-1):
            cur = [0,0]
            cur[0] = max((-p[i]+ prev[1]), prev[0])
            cur[1] = max((p[i]+ prev[0]), prev[1])
            prev=cur
        
        return prev[0]
        



        

