class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # Recursion
        n1,n2=len(text1),len(text2)

        # def subsequence(ind1,ind2):
        #     if ind1<0 or ind2<0:
        #         return 0
            
        #     if text1[ind1]==text2[ind2]:
        #         return 1 + subsequence(ind1-1,ind2-1)
            
        #     return max(subsequence(ind1-1,ind2),subsequence(ind1,ind2-1))

        # return subsequence(n1-1,n2-1)        

        #Memoization
        # dp=[[-1]*n2 for _ in xrange(n1)]
        # def subsequence(ind1,ind2):
        #     if ind1<0 or ind2<0:
        #         return 0
        #     if dp[ind1][ind2]!=-1:
        #         return dp[ind1][ind2]            
        #     if text1[ind1]==text2[ind2]:
        #         dp[ind1][ind2] = 1 + subsequence(ind1-1,ind2-1)
        #         return dp[ind1][ind2]
        #     dp[ind1][ind2] = max(subsequence(ind1-1,ind2),subsequence(ind1,ind2-1))
        #     return dp[ind1][ind2]

        # return subsequence(n1-1,n2-1)        

        #Tabulation
        # dp=[[0]*(n2+1) for _ in xrange(n1+1)]
        
        # for i in xrange(1,len(dp)):
        #     for j in xrange(1,len(dp[0])):
        #         if text1[i-1]==text2[j-1]:
        #             dp[i][j]= 1 + dp[i-1][j-1]
        #         else:
        #             dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        # return dp[n1][n2]

        #Space Optimization
        prev=[0]*(n2+1)

        for i in xrange(1,n1+1):
            cur=[0]*(n2+1)
            for j in xrange(1,n2+1):
                if text1[i-1]==text2[j-1]:
                    cur[j]=1+prev[j-1]
                else:
                    cur[j]=max(prev[j],cur[j-1])
            prev=cur
        return prev[n2]