class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def dfs(node,col,color,graph):
            color[node]=col
            
            for i in graph[node]:
                if color[i]==-1:
                    if dfs(i,not col,color,graph)==False:
                        return False
                elif color[i]==col:
                    return False
            return True


        L=len(graph)
        color=[-1]*L

        for i in range(L):
            if color[i]==-1:
                if dfs(i,0,color,graph)==False:
                    return False
        return True