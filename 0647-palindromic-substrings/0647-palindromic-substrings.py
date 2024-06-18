class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[False]*n for _ in xrange(n)]
        count = 0
        
        for gap in xrange(n):
            for i in xrange(n - gap):
                j = i + gap
                
                if gap == 0:
                    dp[i][j] = True
                elif gap == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
                if dp[i][j]:
                    count += 1
        
        return count
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Tabulation Approach
        
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         count = 0
        
#         for i in range(n):
#             dp[i][i] = True
#             count += 1
        
#         for length in range(2, n + 1):
#             for start in range(n - length + 1):
#                 end = start + length - 1
#                 if length == 2:
#                     dp[start][end] = (s[start] == s[end])
#                 else:
#                     dp[start][end] = (s[start] == s[end]) and dp[start + 1][end - 1]
                
#                 if dp[start][end]:
#                     count += 1
        
#         return count
        
        # Memoization Approach (not working)
        
#         memo = {}
#         dp = [-1]*n
        
#         def checkPalindrome(start, end):
            
#             while start<=end:
#                 if s[start] != s[end]:
#                     return False
#                 start += 1
#                 end -= 1
#             return True
        
        
#         def solve(ind):
#             if ind == n:
#                 return 0
            
#             if ind in memo:
#                 return memo[ind]
            
#             count = 0
#             for i in range(ind, n):
                
#                 if checkPalindrome(ind,i):
#                     count += 1 
            
#             count += solve(ind+1)
#             memo[ind] = count
#             return count
        
#         return solve(0)