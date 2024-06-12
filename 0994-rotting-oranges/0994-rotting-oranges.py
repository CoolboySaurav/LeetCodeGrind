class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        time=0
        fresh=0
        m,n=len(grid),len(grid[0])
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append([i,j])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh>0:
                for i in range(len(q)):
                    r,c=q.popleft()
                    for dr,dc in directions:
                        row,col=r+dr,c+dc
                        if 0<=row<m and 0<=col<n and grid[row][col]==1:
                            grid[row][col]=2
                            q.append([row,col])
                            fresh-=1
                        else:
                            continue
                time+=1
        return time if fresh==0 else -1