class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Dynamic Programming
        n = len(s)
        dp = [[-1]*(n+1) for _ in xrange(n+1)]
        
        def solve(ind, openBracket):
            
            if openBracket < 0:
                return False
            
            if ind == n:
                if openBracket == 0:
                    return True
                else:
                    return False
                
            if dp[ind][openBracket] != -1:
                return dp[ind][openBracket]
            
            if s[ind] == "(":
                dp[ind][openBracket] = solve(ind + 1, openBracket + 1)
                return dp[ind][openBracket]
            elif s[ind] == ")":
                dp[ind][openBracket] = solve(ind+1, openBracket - 1)
                return dp[ind][openBracket]
            else:
                dp[ind][openBracket] = solve(ind+1, openBracket + 1) or solve(ind + 1, openBracket) or solve(ind+1, openBracket -1)
                return dp[ind][openBracket]
        
        return solve(0,0)
        
        
        # Stack solution
        
#         openBracket = []
#         star = []
        
#         for i in xrange(len(s)):
#             if s[i] == "(":
#                 openBracket.append(i)
#             elif s[i] == "*":
#                 star.append(i)
#             else:
#                 if openBracket:
#                     openBracket.pop()
#                 elif star:
#                     star.pop()
#                 else:
#                     return False
        
#         while openBracket:
#             if not star:
#                 return False
#             elif openBracket and star:
#                 if openBracket[-1] < star[-1]:
#                     openBracket.pop()
#                     star.pop()
#                 else:
#                     return False
                
        
#         return  True
        