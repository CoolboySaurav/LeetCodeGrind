class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        q= deque()
        q.append((0,src,0))
        dist = [1e7]*n
        adj = {i:[] for i in xrange(n)}
        dist[src] = 0
        
        for i in flights:
            u, v, cost = i
            adj[u].append((v, cost))
        
        
        while q:
            stop, node, distance = q.popleft()
            
            if stop > k:
                continue
            
            for i in adj[node]:
                nxt, cost = i
                
                if cost + distance < dist[nxt] and stop <=k:
                    dist[nxt] = cost + distance
                    q.append((stop+1, nxt, distance + cost))
                    
                    
        
        return -1 if dist[dst] == 1e7 else dist[dst]
                
            
        
        