class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        
        """
        freq = collections.Counter(nums)
        
        for i in sorted(nums):
            if freq[i] != 0: # If count is 0 means element has been used in previous subsequence
                f = freq[i]
                for j in xrange(i, i + k): 
                    freq[j] -= f # Optimization to quickly skill double counting in case of duplicates
                    if freq[j] < 0:
                        return False
        """
        For example, if certain element has 2 occurances, then its nearby elements must have exactly 2 occurances
        for forming consecutive subsequence. Example: [1,2,3,3,4,4,5,6] here since 3 has 2 occurances, 4 has to have 
        2 occurances to make it work
        
        """
        return True