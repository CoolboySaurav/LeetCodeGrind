class Solution(object):
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
        n= len(p)
        # Recursion solution
        # def find(i,b,txn):
        #     if txn == 3:
        #         return 0
        #     if i == n:
        #         return 0
            
        #     if b == 0:
        #         profit = max((-p[i]+find(i+1,1,txn+1)), find(i+1,0,txn))
        #     else:
        #         profit = max((p[i]+find(i+1,0,txn)), find(i+1,1,txn))
            
        #     return profit
        
        # return find(0,0,0)

        # MEmoization
        # dp= [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        
        # def find(i,b,txn):
        #     if txn == 3:
        #         return 0
        #     if i == n:
        #         return 0
        #     if dp[i][b][txn] != -1:
        #         return dp[i][b][txn] 
        #     if b == 0:
        #         profit = max((-p[i]+find(i+1,1,txn+1)), find(i+1,0,txn))
        #     else:
        #         profit = max((p[i]+find(i+1,0,txn)), find(i+1,1,txn))
            
        #     dp[i][b][txn] = profit
        #     return dp[i][b][txn]  

        # return find(0,0,0)

        #Tabulation
        # dp= [[[0 for _ in range(4)] for _ in range(2)] for _ in range(n+1)]
        
        # for i in xrange(n-1,-1,-1):
        #     for j in xrange(3):
        #         dp[i][0][j]=max((-p[i]+dp[i+1][1][j+1]), dp[i+1][0][j])
        #         dp[i][1][j]=max((p[i]+dp[i+1][0][j]),dp[i+1][1][j])
        # return dp[0][0][0]

        #Space optimization
        prev=[[0 for _ in range(4)] for _ in range(2)]
        cur = [[0 for _ in range(4)] for _ in range(2)]
        
        for i in xrange(n-1,-1,-1): 
            for j in xrange(3):
                cur[0][j]=max((-p[i]+prev[1][j+1]), prev[0][j])
                cur[1][j]=max((p[i]+prev[0][j]),prev[1][j])
                prev = cur
        return prev[0][0]
