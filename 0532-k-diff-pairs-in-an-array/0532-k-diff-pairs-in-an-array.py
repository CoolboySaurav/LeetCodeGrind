class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # HashMap Solution
        numbers = collections.Counter(nums)
        count = 0
        
        if k == 0:
            for key, val in numbers.items():
                if val > 1:
                    count += 1
            return count
    
        for key, val in numbers.items():
            if key + k in numbers:
                count += 1
        
        return count