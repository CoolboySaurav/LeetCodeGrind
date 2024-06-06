class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def find(p):
            if k < 0:
                return 0
            l = r = 0
            count = oddCount = 0

            while r < len(nums):
                if nums[r] % 2:
                    oddCount += 1
                while oddCount > p:
                    if nums[l] % 2:
                        oddCount -= 1
                    l += 1
                count += (r - l + 1)
                r += 1

            return count
        return find(k) - find(k-1)