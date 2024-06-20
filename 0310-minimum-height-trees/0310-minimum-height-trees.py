class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        '''
            There can only be at max 2 nodes with the minimum height since for three nodes, 
            both extremes will have 1 extra depth compared to the central node. So three nodes 
            case gives single node as a answer. For 4 nodes, use induction to find 2 nodes at max.
            Leaves will have signle edge so get rid of leaves then move to the nxt inner layer and 
            repeat the same process until you reach the central node/nodes.
        '''
        
        if not edges:
            return [0]
        
        adj = defaultdict(list)
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        edgeCount = defaultdict(int)
        leaves = deque()
        
        for src, neighbor in adj.items():
            if len(neighbor) == 1:
                leaves.append(src)
            edgeCount[src] = len(neighbor)
            
        
        while leaves:

            if n <= 2:
                return list(leaves)
        # We need to go layer wise for entire graph to eliminate the leaves
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1                
                for neighbor in adj[node]:
                    edgeCount[neighbor] -= 1
                    if edgeCount[neighbor] == 1:
                        leaves.append(neighbor)
                