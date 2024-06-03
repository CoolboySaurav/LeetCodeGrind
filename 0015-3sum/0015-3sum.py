class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        N= len(nums)
        
        # [-4,-1,-1, 0,1,2]
        
        for i in xrange(N):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l = i+1
            r = N-1 
            while l<r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
