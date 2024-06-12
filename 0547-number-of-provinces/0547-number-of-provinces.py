class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        L=len(isConnected[0])
        adj = [[] for _ in range(L)]
        for i in range(L):
            for j in range(L):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
        visit=[0]*L
        def dfs(node,visit,adj):
            visit[node]=1
            for i in adj[node]:
                if not visit[i]:
                    dfs(i,visit,adj)
        count=0
        for i in range(L):
            if not visit[i]:
                count+=1
                dfs(i,visit,adj)
        return count