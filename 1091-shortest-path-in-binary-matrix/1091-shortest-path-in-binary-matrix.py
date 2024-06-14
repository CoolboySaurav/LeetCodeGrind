class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N=len(grid)
        q=deque([(0,0,1)])
        visit=set((0,0))
        direction=[[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

        while q:
            r,c,length=q.popleft()
            if min(r,c)<0 or max(r,c)>=N or grid[r][c]:
                continue
            if r==N-1 and c==N-1:
                return length
            for dr,dc in direction:
                if (r+dr,c+dc) not in visit:
                    q.append((r+dr,c+dc,length+1))
                    visit.add((r+dr,c+dc))
        return -1