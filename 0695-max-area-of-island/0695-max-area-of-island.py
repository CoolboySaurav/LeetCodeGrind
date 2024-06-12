class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R=len(grid)
        C=len(grid[0])
        visit=[[0 for i in range(C)] for j in range(R)]

        def bfs(i,j,count):
            visit[i][j]=1            
            direction=[[-1,0],[1,0],[0,-1],[0,1]]            
            q=deque()
            q.append((i,j))
            count=+1
            while q:
                r,c=q.popleft()
                for dr,dc in direction:
                    row,col=r+dr,c+dc
                    if 0<=row<R and 0<=col<C and not visit[row][col] and grid[row][col]==1:
                        count+=1
                        q.append((row,col))
                        visit[row][col]=1
            return count

        area=0
        for i in range(R):
            for j in range(C):
                if not visit[i][j] and grid[i][j]==1:
                    area=max(bfs(i,j,0),area)
        return area
        
        