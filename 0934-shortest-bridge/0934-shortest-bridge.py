class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        
        N = len(grid)
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        
        def invalid(r, c):
            return r < 0 or c < 0 or r >= N or c >= N
        
        visit = set()
        
        def dfs(i, j):
            if invalid(i, j) or not grid[i][j] or (i, j) in visit:
                return
            visit.add((i, j))
            for dr, dc in direction:
                dfs(i + dr, j + dc)
        
        def bfs():
            res = 0
            q = deque(visit)
            
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direction:
                        row, col = r + dr, c + dc
                        if invalid(row, col) or (row, col) in visit:
                            continue
                        if grid[row][col] == 1:
                            return res
                        q.append((row, col))
                        visit.add((row, col))
                res += 1
        
        found = False
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dfs(r, c) # DFS to travel all the elements of found island
                    found = True
                    break
            if found:
                break
        
        return bfs() # BFS to travel optimally from one island to other
