class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        
        
        
        # BFS Kahn's Algorithm
        indegree=[0]*numCourses
        preCourse={i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preCourse[pre].append(crs)
        
        for i in preCourse:
            for j in preCourse[i]:
                indegree[j]+=1
        
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for i in preCourse[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
            
        return res if len(res)==numCourses else []
