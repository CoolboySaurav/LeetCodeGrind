class Solution(object):
    def coinChange(self, coins, tot):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if tot==0:
            return 0
        if tot in coins:
            return 1
        coins.sort()
        
        n = len(coins)
        
#         def txn(ind, tot):
#             if tot == 0:
#                 return 1
#             if ind == 0:
#                 if coins[ind] == tot:
#                     return 1
#                 else:
#                     return 1e9
#             pick = 1e9
#             if coins[ind] <= tot:
#                 pick = 1 + txn(ind, tot - coins[ind])
#             notPick = txn(ind-1, tot)
            
#             return min(pick, notPick)
        
#         count = txn(n-1, tot)
#         return count if count != 1e9 else -1
    
        dp = [[-1]*(tot+1) for _ in xrange(n)]
        
        def txn(ind, tot):
    
            if ind == 0:
                if tot%coins[ind] == 0:
                    return tot/coins[ind]
                else:
                    return 1e9
            if dp[ind][tot] != -1:
                return dp[ind][tot]
            pick = 1e9
            if coins[ind] <= tot:
                pick = 1 + txn(ind, tot - coins[ind])
            notPick = txn(ind-1, tot)
            
            dp[ind][tot] = min(pick, notPick)
            return dp[ind][tot]
        
        count = txn(n-1,tot)
        return count if count != 1e9 else -1
        
        
        
        
        
        # Recursion 
        # def txn(ind,tot):
        #     if tot==0:
        #         return 0
        #     if tot<0:
        #         return 1e9
        #     if ind<0:
        #         return 1e9
            
        #     pick=1e9
        #     if coins[ind]<=tot:
        #         pick=1+txn(ind,tot-coins[ind])
        #     notPick=txn(ind-1,tot)
        #     return min(pick,notPick)
        
        # count=txn(len(coins)-1,tot)
        # return -1 if count==1e9 else count

        # Memoization
        # dp=[[-1]*(tot+1) for _ in range(len(coins))]
        # def txn(ind,tot):
        #     if ind==0:
        #         if tot%coins[ind]==0:
        #             return tot/coins[ind]
        #         else:
        #             return 1e9
        #     if dp[ind][tot]!=-1:
        #         return dp[ind][tot]
        #     pick=1e9
        #     if coins[ind]<=tot:
        #         pick=1+txn(ind,tot-coins[ind])
        #     notPick=txn(ind-1,tot)
        #     dp[ind][tot] = min(pick,notPick)
        #     return dp[ind][tot]

        # count=txn(len(coins)-1,tot)
        # return -1 if count==1e9 else count
        
        # Tabulation
        # N=len(coins)
        # dp=[[1e9]*(tot+1) for _ in xrange(N)]
        # for i in xrange(tot+1):
        #     if i%coins[0]==0:
        #         dp[0][i]=i/coins[0]
        
        # for i in xrange(1,N):
        #     for j in xrange(tot+1):
        #         notPick=dp[i-1][j]
        #         pick=1e9
        #         if coins[i]<=j:
        #             pick=1+dp[i][j-coins[i]]
        #         dp[i][j]=min(pick,notPick)
        
        # return -1 if dp[N-1][tot]==1e9 else dp[N-1][tot]

        #Space Optimization
        N=len(coins)
        prev=[1e9]*(tot+1)
        cur=[1e9]*(tot+1)
        
        for i in xrange(tot+1):
            if i%coins[0]==0:
                prev[i]=i/coins[0]
        
        for i in xrange(1,N):
            for j in xrange(tot+1):
                notPick=prev[j]
                pick=1e9
                if coins[i]<=j:
                    pick=1+cur[j-coins[i]]
                cur[j]=min(pick,notPick)
            prev=cur
        return -1 if prev[tot]==1e9 else prev[tot]
