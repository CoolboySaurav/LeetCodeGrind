class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = 0
        maxSum = -1e7
        
        for i in nums:
            currSum += i
            maxSum = max(maxSum, currSum)
            if currSum <0:
                currSum = 0 
        
        return maxSum
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         maxSum = nums[0]
#         curSum = 0

#         for n in nums:
#             curSum = max(curSum, 0)
#             curSum += n
#             maxSum = max(maxSum, curSum)
#         return maxSum



        