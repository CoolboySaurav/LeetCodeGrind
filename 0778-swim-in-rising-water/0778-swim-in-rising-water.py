import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = [(grid[0][0], 0, 0)]  # Start with the top-left corner
        visited = set((0, 0))
        
        while q:
            time, row, col = heapq.heappop(q)
            
            if row == col == N - 1:
                return time  # Return the minimum time when reaching the bottom-right corner
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (0 <= r < N) and (0 <= c < N) and (r, c) not in visited:
                    element = (max(time, grid[r][c]), r, c)
                    heapq.heappush(q, element)
                    visited.add((r, c))
