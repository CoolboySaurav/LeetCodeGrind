class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dictionary  = set(wordDict)
        n = len(s)
        
        # Tabulation Approach
        dp = [False]*(n+1)
        dp[n] = True
        
        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                if s[i:j+1] in dictionary:
                    if dp[j + 1]:
                        dp[i] = True
                        break
        return dp[0]       
        
        
        
        # Memoization Approach
        dp = [-1]*n
    
        def helper(ind):
            if ind == n:
                return True
            if dp[ind] != -1:
                return dp[ind]
            
            for i in xrange(ind, n):
                if s[ind:i+1] in dictionary:
                    if helper(i + 1):
                        dp[ind] = True
                        return dp[ind]
            dp[ind] = False
            return dp[ind]
        
        return helper(0)
        
        
        # Recursion Approach
#         def helper(ind):
#             if ind == n:
#                 return True
            
#             for i in xrange(ind, n):
#                 if s[ind:i+1] in dictionary:
#                     if helper(i + 1):
#                         return True
#             return False
        
#         return helper(0)