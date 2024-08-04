class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numMap = {}
        
        for i, v in enumerate(nums):
            if v in numMap and i - numMap[v] <= k:
                return True
            numMap[v] = i
        return False
        
# class Solution:
#     def containsNearbyDuplicate(self, nums, k):
#         window = set()

#         for i in range(len(nums)):
#             if i > k:
#                 window.remove(nums[i - k - 1])
#             if nums[i] in window:
#                 return True
#             window.add(nums[i])
#         return False


