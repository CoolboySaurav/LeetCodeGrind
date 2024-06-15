class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        R = len(heights)
        L = len(heights[0])
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        distance = [[1e7]*L for _ in xrange(R)]
        q = [[0,0,0]]
        distance[0][0] = 0
        heapq.heapify(q)
        
        while q:
            diff, row, col = heapq.heappop(q)
            
            if row == R-1 and col == L-1:
                return distance[R-1][L-1]
            for dr, dc in direction:
                r, c = row + dr, col + dc
                if 0<=r<R and 0<=c<L:
                    newEffort = max(abs(heights[r][c]- heights[row][col]), diff)
                    if newEffort < distance[r][c]:
                        distance[r][c] = newEffort
                        heapq.heappush(q,[newEffort, r, c])
            
        
        
        
        
        # Failed TLE dfs approach
        
#         res = [1e9]
#         visit = set()
        
#         def dfs(row,col, prevNum, currDiff):
#             if row == R-1 and col == L-1:
#                 res[0] = min(res[0],max(currDiff, abs(heights[row][col] - prevNum)))
#                 return 
            
#             visit.add((row,col))
            
#             for dr,dc in direction:
#                 r = row + dr
#                 c = col + dc
                
#                 if 0 <= r < R and 0 <= c < L and (r,c) not in visit:
#                     dfs(r,c, heights[r][c], max(currDiff, abs(heights[r][c] - heights[row][col])))
            
#             visit.remove((row,col))
        
        
#         dfs(0,0, heights[0][0], -1e7)
                        
#         return res[0]
        
        
        