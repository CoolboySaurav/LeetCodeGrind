class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Always keep the longest palindromic subsequence and 
        # add/reaarange other characters of the string in order to minimize the operations
        n=len(s)
        t=s[::-1]
        prev=[0]*(n+1)

        for i in xrange(1,n+1):
            cur=[0]*(n+1)
            for j in xrange(1,n+1):
                if s[i-1]==t[j-1]:
                    cur[j]=1+prev[j-1]
                else:
                    cur[j]=max(prev[j],cur[j-1])
            prev=cur
        
        return n-prev[n]