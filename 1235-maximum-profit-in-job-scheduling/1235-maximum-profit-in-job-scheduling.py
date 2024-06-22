class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        n = len(profit)
        
        intervals = sorted(zip(startTime, endTime, profit))
        
        cache = {}
        
        def solve(i):
            if i == n:
                return 0
            if i in cache:
                return cache[i]
            
            # Not Pick
            res = solve(i+1)
        
            # Pick
            # Binary Search to find startTime greater than current endTime
            l = i + 1
            r = n - 1
            ans = n
            
            while l <= r:
                mid = (l+r)//2
                
                if intervals[mid][0] >= intervals[i][1]:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
                            
            cache[i] = res = max(res, intervals[i][2] + solve(ans))
            return cache[i]
        
            
        return solve(0)
        
        
        
        
        
        # Recusion Structure
        
#         def solve(ind, prevStart):
#             if ind < 0:
#                 return 0
                
#             pick = 0
#             if endTime[ind] <= prevStart:
#                 pick = profit[ind] + solve(ind-1, startTime[ind])
#             notPick = 0 + solve(ind -1, prevStart)
            
#             return max(pick, notPick)
        
#         return solve(n-1, float('inf'))
    
        # Memoization Solution (Not Working)
        
#         dp = [[-1]*(n+1) for _ in xrange(n)]
        
#         def solve(ind, prevInd):
#             if ind < 0:
#                 return 0
            
#             if dp[ind][prevInd] != -1:
#                 return dp[ind][prevInd]
                
#             pick = 0
#             if prevInd == n or endTime[ind] <= startTime[prevInd]:
#                 pick = profit[ind] + solve(ind-1, ind)
#             notPick = 0 + solve(ind -1, prevInd)
            
#             dp[ind][prevInd] =  max(pick, notPick)
#             return dp[ind][prevInd]
        
#         return solve(n-1,n)
    