class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefixSum = []
        self.total = 0
        
        for i,v in enumerate(w):
            self.total += v
            self.prefixSum.append(self.total)
        

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.uniform(0, self.total)
        
        l, r = 0, len(self.prefixSum)  - 1
        
        while l < r:
            mid = (l + r) // 2
            if self.prefixSum[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()