class Solution(object):
    def shortestCommonSupersequence(self, s1, s2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
    # Finding longest common subsequence
        a,b=len(s1),len(s2)
        dp=[[0]*(b+1) for _ in xrange(a+1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
    #####################################################
        res=""
        i,j=a,b
        while i>0 and j>0:
            if s1[i-1]==s2[j-1]:
                res+=s1[i-1]
                i-=1
                j-=1
            elif dp[i][j-1]>dp[i-1][j]:
                res+=s2[j-1]
                j-=1
            else:
                res+=s1[i-1]
                i-=1
        if i>0:
            p=s1[:i]
            res+=p[::-1]
        else:
            p=s2[:j]
            res+=p[::-1]
        return res[::-1]