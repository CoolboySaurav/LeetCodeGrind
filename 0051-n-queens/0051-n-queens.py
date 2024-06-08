class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board=["."*n for i in range(n)]
        # board=[None]*n
        # s="."*n
        # for i in range(n):
        #     board[i]=s
        # Following are the only directions to check whether the queen exist or no
        upperDiagonal=[0]*(2*n - 1) # 2n-1 from the the max value for the formula n-1 + (col-row)
        lowerDiagonal=[0]*(2*n - 1) # 2n-1 from the max value for the formula col+row
        left=[0]*n
        res=[]
        
        def solve(col, upper,lower,lrow,res):
            if col==n:
                res.append(board[:])
                return 
            for i in range(n):
                if lrow[i]==0 and upper[n-1+col-i]==0 and lower[col+i]==0:
                    lrow[i]=1
                    upper[n-1+col-i]=1
                    lower[col+i]=1
                    board[i]=board[i][:col]+'Q'+board[i][col+1:]
                    solve(col+1,upper,lower,lrow,res)
        # Backtracking 
                    lrow[i]=0
                    upper[n-1+col-i]=0
                    lower[col+i]=0
                    board[i]=board[i][:col]+'.'+board[i][col+1:]
        
        solve(0,upperDiagonal,lowerDiagonal,left,res)
        return res
