class Solution(object):
    def advantageCount(self, nums1, nums2):
        
        """
        Sort the both arrays first. If the max of nums1 is greater than max of nums2 then no issue.
        If its not the case, we will put the min of nums1 to the placeholder for respective max of nums2
        """
        
        
        nums1.sort()
        nums2 = sorted([(v, i) for i, v in enumerate(nums2)])
        N = len(nums1)
        l , r = 0, N - 1
        result = [-1]*N
        
        for i in xrange(N-1, -1, -1):
            if nums1[r] > nums2[i][0]:
                result[nums2[i][1]] = nums1[r]
                r -= 1
            else:
                result[nums2[i][1]] = nums1[l]
                l += 1
        
        return result
        