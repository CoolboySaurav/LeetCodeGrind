class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n=len(matrix)
        

        if n==1:
            return matrix[0][0] 

        for i in xrange(1,n):
            for j in xrange(n):
                ld=u=rd=1e7
                if j>=1:
                    ld=matrix[i][j]+matrix[i-1][j-1]
                u=matrix[i][j]+matrix[i-1][j]
                if j<n-1:
                    rd=matrix[i][j]+matrix[i-1][j+1]
                matrix[i][j]=min(ld,u,rd)
                
        return min(matrix[n-1])