class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res= []
        i = 1
        res.append([1])
        while i < numRows:
            
            level = []
            
            for j in range(i+1):
                a = 0
                b = 0
                if j > 0:
                    a = res[i-1][j-1]
                if j <= i - 1:
                    b = res[i-1][j]
                
                level.append(a+b)
            res.append(level)
            i += 1
        
        return res