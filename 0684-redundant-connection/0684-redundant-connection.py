from collections import defaultdict

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = defaultdict(list)
        
        def hasCycle(node, parent):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if hasCycle(nei, node):
                        return True
                elif nei != parent:
                    return True
            return False
        
        for a, b in edges:
            visited = set()
            adj[a].append(b)
            adj[b].append(a)
            
            # Check if adding this edge creates a cycle
            if hasCycle(a, -1):
                return [a, b]
        
        return []
