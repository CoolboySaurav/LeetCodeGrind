class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        freq = collections.Counter(nums)
        
        for i in sorted(nums):
            if freq[i] != 0:
                f = freq[i]
                for j in xrange(i, i + k):
                    freq[j] -= f
                    if freq[j] < 0:
                        return False
        return True