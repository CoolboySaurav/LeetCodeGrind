class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        a,b = len(s),len(t)
        # Recursion
        # def find(i,j):
        #     if j<0:
        #         return 1
        #     if i<0:
        #         return 0

        #     if s[i]==t[j]:
        #         return find(i-1,j-1)+find(i-1,j)
        #     else:
        #         return find(i-1,j)
        # return find(a-1,b-1)

        #Memoization
        # dp = [[-1]*(b) for _ in xrange(a)]
        # def find(i,j):
        #     if j<0:
        #         return 1
        #     if i<0:
        #         return 0
        #     if dp[i][j]!=-1:
        #         return dp[i][j]

        #     if s[i]==t[j]:
        #         dp[i][j] = find(i-1,j-1)+find(i-1,j)
        #         return dp[i][j]
            
        #     dp[i][j] = find(i-1,j)
        #     return dp[i][j]
        # return find(a-1,b-1)

        #Tabulation
        # dp = [[0]*(b+1) for _ in xrange(a+1)]
        # #Base case 
        # for i in xrange(a+1):
        #     dp[i][0] =  1
        
        # for i in xrange(1,a+1):
        #     for j in xrange(1,b+1):
        #         if s[i-1] == t[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j]
        
        # return dp[a][b]

        #Space Optimization
        prev = [0]*(b+1)
        prev[0] = 1

        for i in xrange(1,a+1):
            cur = [0]*(b+1)
            cur[0] = 1
            for j in xrange(1,b+1):
                if s[i-1] == t[j-1]:
                    cur[j] = prev[j-1] + prev[j]
                else:
                    cur[j] = prev[j]
            prev = cur

        return prev[b]