class Solution(object):
    def spiralOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        t = l = 0
        r = len(mat[0])
        b = len(mat) 
        res = []
        dr, dc = 0 , 1
        i = j = 0
        while l < r and t < b:
            #left -> right
            for i in range(l,r):
                res.append(mat[t][i])
            t+=1
            #top -> bot
            for i in range(t, b):
                res.append(mat[i][r-1])
            r-=1

            if not (l<r and t<b):
                break

            #right -> left
            for i in range(r-1,l-1,-1):
                res.append(mat[b-1][i])
            b-=1
            #bot -> top
            for i in range(b-1,t-1,-1):
                res.append(mat[i][l])
            l+=1
        
        return res
