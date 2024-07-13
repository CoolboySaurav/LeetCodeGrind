class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True