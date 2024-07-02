class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n==0:
            return len(tasks)
        hash1=Counter(tasks)
        maxheap=[-cnt for cnt in hash1.values()]
        heapq.heapify(maxheap)
        time=0
        q=deque()
        while maxheap or q:
            time+=1
            if maxheap:
                p=heapq.heappop(maxheap)+1
                if p:
                     q.append([p,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time