class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def find(nums,k):
            prev=[False]*(k+1)
            prev[0]=True
            if nums[0]<k:
                prev[nums[0]]=True

            for i in range(1,len(nums)):
                cur=[False]*(k+1)
                cur[0]=True
                for target in range(1,k+1):
                    notPick=prev[target]        
                    pick=False
                    if nums[i]<=target:
                        pick=prev[target-nums[i]]
                    cur[target]=pick or notPick
                prev=cur
            return prev[k]

        totSum=0
        for i in nums:
            totSum+=i
        if totSum%2: return False
        K=totSum/2
        
        return find(nums, K)
        