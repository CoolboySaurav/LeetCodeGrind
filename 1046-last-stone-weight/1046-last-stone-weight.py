class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones)==1:
            return stones[0]
        heap=[-i for i in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            x=heapq.heappop(heap)
            if len(heap)>=1:
                y=heapq.heappop(heap)
                if abs(x-y)>0:
                    heapq.heappush(heap,-abs(x-y))
        if heap:
            return -heap[0]
        else:
            return 0