class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        def dfs(node, pathVisit, visit, check, graph):
            visit[node] = 1
            pathVisit[node] = 1
            check[node] = 0
            
            for i in graph[node]:
                if not visit[i]:
                    if dfs(i,pathVisit, visit, check, graph) == True:
                        return True
                elif pathVisit[i] == 1:
                    return True
            
            check[node] = 1
            pathVisit[node] = 0
            return False
        
        
        
        L = len(graph)
        pathVisit = [0]*L
        visit = [0]*L
        res = []
        check = [0]*L
        
        for i in xrange(L):
            if not visit[i]:
                dfs(i,pathVisit,visit,check, graph)
        
        for i in xrange(L):
            if check[i] == 1:
                res.append(i)
        
        return res
         
