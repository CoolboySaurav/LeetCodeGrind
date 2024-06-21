class MedianFinder(object):

    def __init__(self):
        
        self.small, self.large = [], []
        # small is smaller numbers with max heap implementation
        # large is larger numbers with min heap implementation
        # For median, we can get max of small and min of large in O(1)
        # All the elements of large are almost greater than elements of small
        # At max, we allow length of either heap to exceed by at max of 1 at any case
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -1*num)
        
        if self.small and self.large and (-1* self.small[0]) > self.large[0]:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*val)
            
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return -1* self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (self.large[0] + (-1 * self.small[0]))/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian() 