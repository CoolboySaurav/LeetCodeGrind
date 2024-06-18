class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        # Recursion
        # def find(cur,prev):
        #     #Base case
        #     if cur>=n:
        #         return 0
        #     pick = -1e7
        #     notPick = find(cur+1,prev)
        #     if nums[cur]>nums[prev] or prev == -1:
        #         pick = 1 + find(cur+1, cur)
            
        #     return max(pick,notPick)
        
        #return find(0,-1)

        # Memoization
        # dp=[[-1]*(n+1) for _ in xrange(n)]
        # def find(cur,prev):
        #     #Base case
        #     if cur>=n:
        #         return 0
        #     if dp[cur][prev+1] != -1:
        #         return dp[cur][prev+1]
    
        #     length = find(cur+1,prev)
        #     if nums[cur]>nums[prev] or prev == -1:
        #         length = max(length, 1 + find(cur+1, cur))
            
        #     dp[cur][prev+1]= length
        #     return dp[cur][prev+1]

        # return find(0,-1)
    
        #Tabulation
        # dp = [[0]*(n+1) for _ in xrange(n+1)]
        
        # for cur in xrange(n-1,-1,-1):
        #     for prev in xrange(cur-1,-2,-1):
        #         length = dp[cur+1][prev+1]
        #         if nums[cur]>nums[prev] or prev == -1:
        #             length = max(length, 1 + dp[cur+1][cur+1])
                
        #         dp[cur][prev+1]= length

        # return dp[0][-1+1]                

        # Space Optimization

        nex = [0]*(n+1)
        curr = [0]*(n+1)

        for cur in xrange(n-1,-1,-1):
            for prev in xrange(cur-1,-2,-1):
                length = nex[prev+1]
                if nums[cur]>nums[prev] or prev == -1:
                    length = max(length, 1 + nex[cur+1])
                
                curr[prev+1]= length

            nex=curr
        return nex[-1+1]                

