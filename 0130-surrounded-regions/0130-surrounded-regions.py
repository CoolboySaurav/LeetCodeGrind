class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        q=deque()
        m=len(board)
        n=len(board[0])
        visit=[[0 for _ in range(n)] for _ in range(m)]
        # Only show interest in those O which are on the edges
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1) and board[i][j]=="O":
                    q.append((i,j))
                    visit[i][j]=1
                if (j==0 or j==n-1) and board[i][j]=="O":
                    q.append((i,j))
                    visit[i][j]=1
        # If q is empty, that means no edge O present 
        if not q:
            for i in range(m):
                for j in range(n):
                    board[i][j]="X"
            return None
        direction=[[0,-1],[0,1],[1,0],[-1,0]]
        while q:
            r,c=q.popleft()
            for dr,dc in direction:
                row,col=r+dr,c+dc
                if 0<=row<m and 0<=col<n and board[row][col]=="O" and not visit[row][col]:
                    visit[row][col]=1
                    q.append((row,col))
        for i in range(m):
            for j in range(n):
                if not visit[i][j] and board[i][j]=="O":
                    board[i][j]="X"
        return None

