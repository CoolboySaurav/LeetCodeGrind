class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        land_count = 0

        # Step 1: Count land cells and enqueue border cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    land_count += 1
                    if r in [0, rows-1] or c in [0, cols-1]:
                        queue.append((r, c))

        # Step 2: BFS from the border cells
        while queue:
            r, c = queue.popleft()
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 0  # Mark as visited
                land_count -= 1
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))

        # Step 3: Return the count of enclaved land cells
        return land_count



        # def dfs(i,j,visit,direction):
        #     visit[i][j]=1
        #     for dr,dc in direction:
        #         row,col=i+dr,j+dc
        #         if 0<=row<R and 0<=col<C and not visit[row][col] and grid[row][col]==1:
        #             dfs(row,col,visit,direction)




        # R=len(grid)
        # C=len(grid[0])
        # direction=[[1,0],[-1,0],[0,1],[0,-1]]
        # visit=[[0 for i in range(C)] for j in range(R)]
        # for i in range(R):
        #     # Row wise travel through first column
        #     if not visit[i][0] and grid[i][0]==1:
        #         dfs(i,0,visit,direction)
        #     # Row wise travel through last column
        #     if not visit[i][C-1] and grid[i][C-1]==1:
        #         dfs(i,C-1,visit,direction)
        
        # for j in range(C):
        #     # Column wise travel through first row
        #     if not visit[0][j] and grid[0][j]==1:
        #         dfs(0,j,visit,direction)
        #     # Column wise travel through last row
        #     if not visit[R-1][j] and grid[R-1][j]==1:
        #         dfs(R-1,j,visit,direction)
        
        # count=0
        # for i in range(R):
        #     for j in range(C):
        #         if not visit[i][j] and grid[i][j]==1:
        #             count+=1
        # return count
