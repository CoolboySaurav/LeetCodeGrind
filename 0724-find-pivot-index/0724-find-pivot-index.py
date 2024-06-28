class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ind = -1
        n = len(nums)
        
        prefixSum = [0]*n
        prefixSum[0] = nums[0]
        
        for i in xrange(1,n):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        
        
        for i in xrange(n):
            left = 0
            if i > 0:
                left = prefixSum[i-1]
            right = prefixSum[-1] - prefixSum[i]
            
            if left == right:
                ind = i
                return ind
        
        return ind