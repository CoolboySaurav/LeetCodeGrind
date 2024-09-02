class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        # Recursion Solution (TLE)
#         def solve(ind, b):
#             if ind >= n:
#                 return 0
#             profit = 0
            
#             if not b:
#                 profit = max(solve(ind + 1, 0), -prices[ind] + solve(ind + 1, 1))
#             else:
#                 profit = max(solve(ind + 1, 1), prices[ind] + solve(ind + 2, 0))
            
#             return profit
        
#         return solve(0, 0)

        # Memoization Solution
        dp = [[-1] * (2) for _ in range(n)]
        def solve(ind, b):
            if ind >= n:
                return 0
            if dp[ind][b] != -1:
                return dp[ind][b]
            profit = 0
            
            if not b:
                profit = max(solve(ind + 1, 0), -prices[ind] + solve(ind + 1, 1))
            else:
                profit = max(solve(ind + 1, 1), prices[ind] + solve(ind + 2, 0))
            dp[ind][b] = profit
            return dp[ind][b]
        
        return solve(0, 0)
        
        