class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # """
        # if len(nums)==1:
        #     return nums[0]
        # for i in range(len(nums)):
        #     if (nums[i] not in nums[i+1:]) and (nums[i] not in nums[:i]):
        #         return nums[i]
        result = 0
        
        for num in nums:
            result ^= num
        
        return result