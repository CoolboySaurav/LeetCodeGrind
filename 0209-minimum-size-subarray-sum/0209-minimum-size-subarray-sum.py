class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        if target == nums[0]:
            return 1
        
        l = r = 0
        minLen = float('inf')
        curSum = 0
        
        while r < len(nums):
            curSum += nums[r]
            while curSum > target:
                if curSum >= target:
                    minLen = min(minLen, (r - l + 1))
                curSum -= nums[l]
                l += 1
            if curSum >= target:
                minLen = min(minLen, (r - l + 1))    
            r += 1
        
        return minLen if minLen != float('inf') else 0