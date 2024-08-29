class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        
        for i in range(n - 1, -1, -1):
            count =  0
            
            for j in range(i, n):
                p = s[i:j + 1]
                
                if 0 < int(p) <= 26 and int(p[0]) != 0:
                    count += dp[j + 1]
                
            dp[i] = count
        
        return dp[0]
        
        
        
        n = len(s)
        memo = {}
        def helper(ind):
            if ind == n:
                return 1
            if ind in memo:
                return memo[ind]
            count = 0
            
            for i in range(ind, n):
                p = s[ind:i+1]
                
                if  0 < int(p) <= 26 and int(p[0]) != 0:
                    count += helper(i + 1)
            memo[ind] = count
            return count
        
        return helper(0)