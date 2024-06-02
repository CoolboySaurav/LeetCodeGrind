class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        output = [] 
        
        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        
        for i in range(len(nums)): 
            if 0 < i < len(nums) - 1:
                output.append(prefix[i - 1] * suffix[i + 1])
            elif i == 0: 
                output.append(suffix[i + 1])
            else:
                output.append(prefix[i - 1])
        return output        