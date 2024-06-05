class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        zero = 0 
        maxlen = 0

        for r in xrange(len(nums)):
            if nums[r] == 0:
                zero += 1
            if zero <= k:
                maxlen = max( maxlen, r-l+1)
            else:
                while zero > k:
                    if nums[l] ==0:
                        zero -= 1
                    l += 1
        return maxlen         