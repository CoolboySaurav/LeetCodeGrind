class Solution:
    def numDecodings(self, s: str) -> int:
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