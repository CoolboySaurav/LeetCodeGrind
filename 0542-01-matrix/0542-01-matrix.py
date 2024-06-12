class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(mat)
        n=len(mat[0])
        visit = [[0 for _ in range(n)] for _ in range(m)]
        res =  [[float("inf") for _ in range(n)] for _ in range(m)] 
        q=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    res[i][j]=0
                    visit[i][j]=1
        direction=[[0,-1],[0,1],[1,0],[-1,0]]
        while q:
            r,c,d=q.popleft()
            for dr,dc in direction:
                row,col=r+dr,c+dc
                if 0<=row<m and 0<=col<n and mat[row][col]==1 and not visit[row][col]:
                    q.append((row,col,d+1))
                    visit[row][col]=1
                    res[row][col]=d+1 
        return res        
        