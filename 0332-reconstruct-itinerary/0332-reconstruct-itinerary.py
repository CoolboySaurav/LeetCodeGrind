class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        
        for a, b  in tickets:
            adj[a].append(b)
        
        for val in adj.values():
            val.sort(reverse = True)
        
        res = []
        
        def dfs(node):
            #dest = adj[node]
            
            while adj[node]:
                nxt = adj[node].pop()
                dfs(nxt)
            
            res.append(node)
        
        dfs("JFK")
        
        return res[::-1]
        