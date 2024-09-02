class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        
        # Optimization for cases where k >= n // 2 (can trade on every day)
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit

        dp = [[[-1] * (k + 1) for _ in range(2)] for _ in range(n)]
        
        def solve(i, b, txn):
            if txn == k:
                return 0
            if i == n:
                return 0
            if dp[i][b][txn] != -1:
                return dp[i][b][txn]
            
            profit = 0
            if b == 0:
                # Option 1: Buy stock, increase txn count
                # Option 2: Skip buying
                profit = max(-prices[i] + solve(i + 1, 1, txn), solve(i + 1, b, txn))
            else:
                # Option 1: Sell stock, increase txn count
                # Option 2: Skip selling
                profit = max(prices[i] + solve(i + 1, 0, txn + 1), solve(i + 1, b, txn))
            
            dp[i][b][txn] = profit
            return dp[i][b][txn]

        return solve(0, 0, 0)
