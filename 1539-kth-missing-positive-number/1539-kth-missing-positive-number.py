class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        
        l, r = 0, len(arr) - 1
        
        while l <= r:
            mid = (l+r)//2
            
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                l = mid + 1
            else:
                r = mid - 1
        
        return r + 1 + k