class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        pq = [(0, 0)]
        adj = defaultdict(list)
        time = [float('inf')] * n
        time[0] = 0
        ways = [0] * n
        ways[0] = 1
        mod = int(1e9 + 7)
        
        for u, v, t in roads:
            adj[u].append([v, t])
            adj[v].append([u, t])
        
        while pq:
            dist, node = heapq.heappop(pq)
            
            for nei, t in adj[node]:
                if t + dist < time[nei]:
                    time[nei] = t + dist
                    heapq.heappush(pq, (time[nei], nei))
                    ways[nei] = ways[node] % mod
                elif t + dist == time[nei]:
                    ways[nei] = (ways[nei] + ways[node] ) % mod
        
        return ways[n - 1]