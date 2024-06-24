class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Striver - Greedy
        maxInd = 0
        
        for i in xrange(len(nums)):
            if i > maxInd:
                return False
            maxInd = max( maxInd, i + nums[i])
        
        return True
        
        
        
        
        #Greedy
        goal=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=goal:
                goal=i
            
        if goal==0:
            return True
        else:
            return False
            