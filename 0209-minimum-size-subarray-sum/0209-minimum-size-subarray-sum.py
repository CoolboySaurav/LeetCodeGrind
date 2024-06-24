class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        l = r = 0
        minLen = float('inf')
        curSum = nums[0]
        
        while r < len(nums):
            if curSum >= target:
                minLen = min( minLen, r - l + 1)
                curSum -= nums[l]
                l += 1
            else:
                r += 1
                if r == len(nums):
                    break
                curSum += nums[r]
        
        return minLen if minLen != float('inf') else 0