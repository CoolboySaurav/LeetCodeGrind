class Solution(object):
    def minDistance(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a,b=len(w1),len(w2)
        # Recursion
        # def find(i,j,s1,s2):
        #     #Base Case
        #     if j<0:
        #         return i+1
        #     if i<0:
        #         return j+1

        #     if s1[i] == s2[j]:
        #         return 0 + find(i-1,j-1,s1,s2)
            
        #     insert = 1 + find(i,j-1,s1[:i+1]+s2[j]+s1[i+1:],s2)
        #     replace = 1 + find(i-1,j-1,s1[:i]+s2[j]+s1[i+1:],s2)
        #     remove = 1 + find(i-1,j,s1[:i]+s1[i+1:],s2)



        #     return min(replace,remove,insert)
        
        # return find(a-1,b-1,w1,w2)

        # Memoization

        # dp=[[-1]*b for _ in xrange(a)]
        # def find(i,j,s1,s2):
        #     #Base Case
        #     if j<0:
        #         return i+1
        #     if i<0:
        #         return j+1
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     if s1[i] == s2[j]:
        #         dp[i][j] = 0 + find(i-1,j-1,s1,s2)
        #         return dp[i][j]
                    
        #     insert = 1 + find(i,j-1,s1[:i+1]+s2[j]+s1[i+1:],s2)
        #     replace = 1 + find(i-1,j-1,s1[:i]+s2[j]+s1[i+1:],s2)
        #     remove = 1 + find(i-1,j,s1[:i]+s1[i+1:],s2)

        #     dp[i][j] = min(replace,remove,insert)
        #     return dp[i][j]

        # return find(a-1,b-1,w1,w2)

        # Tabulation
        # dp=[[1e9]*(b+1) for _ in xrange(a+1)]

        # for i in xrange(a+1):
        #     dp[i][0]=i
        
        # for j in xrange(b+1):
        #     dp[0][j]=j
        
        # for i in xrange(1,a+1):
        #     for j in xrange(1,b+1):
        #         if w1[i-1] == w2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             insert = 1 + dp[i][j-1]
        #             replace = 1 + dp[i-1][j-1]
        #             remove = 1 + dp[i-1][j]
        #             dp[i][j]=min(insert,replace,remove)
        
        # return dp[a][b]

        #Space Optimization
        prev=[0]*(b+1)
        
        for j in xrange(b+1):
            prev[j]=j
        
        for i in xrange(1,a+1):
            cur=[0]*(b+1)
            cur[0]=i
            for j in xrange(1,b+1):
                if w1[i-1]==w2[j-1]:
                    cur[j]=prev[j-1]
                else:
                    insert= 1 + cur[j-1]
                    replace=1 + prev[j-1]
                    remove= 1 + prev[j]
                    cur[j]= min(insert,remove,replace)
            prev=cur
        return prev[b]