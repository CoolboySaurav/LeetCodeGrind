class Solution(object):
    def canFinish(self, n, pre):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # DFS Striver way
#         def dfs(node, visit, pathVisit):
#             visit[node] = 1
#             pathVisit[node] = 1
            
#             for i in adj[node]:
#                 if not visit[i]:
#                     if dfs(i, visit, pathVisit):
#                         return True
#                 elif pathVisit[i]:
#                     return True
            
#             pathVisit[node] = 0
#             return False
        
#         visit = [0]*n
#         pathVisit = [0]*n
#         adj = { i:[] for i in range(n)}
        
#         for crs, prereq in pre:
#             adj[crs].append(prereq)
        
        
#         for i in xrange(n):
#             if not visit[i]:
#                 if dfs(i, visit, pathVisit):
#                     return False
        
#         return True

        # BFS Kahn's Algorithm
        
        indegree = [0]*n
        adj = { i:[] for i in range(n)}
        
        for crs, prereq in pre:
            adj[crs].append(prereq)

        for i in xrange(n):
            for j in adj[i]:
                indegree[j] += 1
        
        q = deque()
        
        for i in xrange(n):
            if not indegree[i]:
                q.append(i)
                
        count = 0
        
        while q:
            node = q.popleft()
            
            for i in adj[node]:
                indegree[i] -= 1
                if not indegree[i]:
                    q.append(i)
            count += 1
        
        return count == n         
        
        
        
        
        
        
        
        
        
        
        
        
        
# NEETCODE DFS with higher optimization

        # visit=set()
        # preCourse={i:[] for i in range(numCourses)}
        # for crs,pre in prerequisites:
        #     preCourse[crs].append(pre)

        # def dfs(crs):
        #     if crs in visit:
        #         return False
        #     if not preCourse[crs]:
        #         return True
        #     visit.add(crs)
        #     for pre in preCourse[crs]:
        #         if dfs(pre)==False:
        #             return False
        #     visit.remove(crs)
        #     preCourse[crs]=[]
        #     return True

        
        # for crs in range(numCourses):
        #     if dfs(crs)==False:
        #         return False
        # return True

# BFS with higher space complexity
#         preCourse={i:[] for i in range(numCourses)}
#         for crs,pre in prerequisites:
#             preCourse[crs].append(pre)
#         indegree=[0]*len(preCourse)
#         for i in preCourse:
#             for j in preCourse[i]:
#                 indegree[j]+=1

#         q=deque() 
#         for i in range(numCourses):
#             if indegree[i]==0:
#                 q.append(i)
#         res=[]
#         while q:
#             node=q.popleft()
#             res.append(node)
#             for i in preCourse[node]:
#                 indegree[i]-=1
#                 if indegree[i]==0:
#                     q.append(i)
#         return len(res)==numCourses