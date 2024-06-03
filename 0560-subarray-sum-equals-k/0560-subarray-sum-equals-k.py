class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        currSum = 0
        count = 0
        
        for i in nums:
            currSum += i
            if (currSum - k) in prefixSum:
                count += prefixSum[(currSum - k)]
            prefixSum[currSum] += 1
        
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         prefix=defaultdict()
#         preSum=count=0
#         prefix[0]=1
#         for i in nums:
#             preSum+=i
#             if preSum-k in prefix:
#                 count+=prefix[preSum-k]
#             if preSum in prefix:
#                 prefix[preSum]+=1
#             else:
#                 prefix[preSum]=1
        
#         return count