class Solution(object):
    def change(self, tot, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n=len(coins)
        
        # Recursion
        # def find(ind,tar):
        #     if ind==0:
        #         if tar%coins[ind]==0:
        #             return 1
        #         else:
        #             return 0
        #     notPick=find(ind-1,tar)
        #     pick=0
        #     if coins[ind]<=tar:
        #         pick=find(ind,tar-coins[ind])
            
        #     return pick + notPick
        
        # return find(n-1,tot)

        #Memoization
        # dp=[[-1]*(tot+1) for _ in range(len(coins))]
        # def find(ind,tar):
        #     if tar==0:
        #         return 1
        #     if ind==0:
        #         if tar%coins[ind]==0:
        #             return 1
        #         else:
        #             return 0
        #         if dp[ind][tar]!=-1:
        #             return dp[ind][tar]
        #     notPick=find(ind-1,tar)
        #     pick=0
        #     if coins[ind]<=tar:
        #         pick=find(ind,tar-coins[ind])
            
        #     dp[ind][tar]=pick + notPick
        #     return dp[ind][tar]
        
        # return find(n-1,tot)

        # Tabulation
        # dp=[[0]*(tot+1) for _ in xrange(n)]
        # for i in xrange(tot+1):
        #     if i%coins[0]==0:
        #         dp[0][i]=1
        
        # for i in xrange(1,n):
        #     for j in xrange(tot+1):
        #         notPick=dp[i-1][j]
        #         pick=0
        #         if coins[i]<=j:
        #             pick=dp[i][j-coins[i]]
        #         dp[i][j]=pick + notPick
        # return dp[n-1][tot]

        #Space Optimization
        prev=[0]*(tot+1)
        for i in xrange(tot+1):
            if i%coins[0]==0:
                prev[i]=1
        
        for i in xrange(1,n):
            cur=[0]*(tot+1)
            for j in xrange(tot+1):
                notPick=prev[j]
                pick=0
                if coins[i]<=j:
                    pick=cur[j-coins[i]]
                cur[j]=pick + notPick
            prev=cur
        return prev[tot]