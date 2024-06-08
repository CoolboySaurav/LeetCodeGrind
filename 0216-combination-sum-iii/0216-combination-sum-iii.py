class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = list(range(1,10))
        res = []
        
        def find(i,arr, target):
            if len(arr) == k:
                if target == 0:
                    res.append(arr)
                    return 
            
            for j in xrange(i,len(nums)):
                if nums[j] > target:
                    break
                find(j+1,arr + [nums[j]], target- nums[j])
        
        find(0,[],n)
        return res