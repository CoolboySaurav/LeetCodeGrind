class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        heap = [(0, 0)]
        in_MST = [False] * n
        mstCost = 0
        numEdges = 0
        
        while numEdges < n:
            weight, node = heapq.heappop(heap)
            if in_MST[node]:
                continue
            in_MST[node] = True
            mstCost += weight
            numEdges += 1
            
            for nxt in range(n):
                if not in_MST[nxt]:
                    nxt_wt = abs(points[node][0] - points[nxt][0]) + abs(points[node][1] - points[nxt][1])
                    heapq.heappush(heap, (nxt_wt, nxt))
        return mstCost