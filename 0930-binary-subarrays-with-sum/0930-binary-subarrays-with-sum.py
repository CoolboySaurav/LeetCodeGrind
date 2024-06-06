class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def find(k):
            if k < 0:
                return 0
            
            l = r = 0
            count = 0
            currSum = 0
            
            while r < len(nums):
                currSum += nums[r]
                while currSum > k:
                    currSum -= nums[l]
                    l += 1
                count += (r - l + 1)
                r += 1
            return count
        
        return find(goal) - find(goal-1)