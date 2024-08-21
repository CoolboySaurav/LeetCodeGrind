class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [ - i for i in nums]
        n = len(nums)
        heapq.heapify(heap)        
        while len(heap) > n - k + 1:
            heapq.heappop(heap)
        
        return - heap[0]