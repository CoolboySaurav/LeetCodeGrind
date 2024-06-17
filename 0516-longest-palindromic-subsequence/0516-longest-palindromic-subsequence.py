class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        t=s[::-1]

        #dp=[[0]*(n+1) for _ in xrange(n+1)]

        prev=[0]*(n+1)

        for i in xrange(1,n+1):
            cur=[0]*(n+1)
            for j in xrange(1,n+1):
                if s[i-1]==t[j-1]:
                    cur[j]=1+prev[j-1]
                else:
                    cur[j]=max(prev[j],cur[j-1])
            prev=cur
        return prev[n]                    