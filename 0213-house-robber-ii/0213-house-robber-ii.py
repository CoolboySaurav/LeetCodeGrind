class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return nums[0]
# House Robber I solution is used here
        def rob1(nums):
            prev2=0
            prev=nums[0]

            for i in range(1,len(nums)):
                curr=max(nums[i]+prev2,prev)
                prev2=prev
                prev=curr
            return prev
        
        return max(rob1(nums[0:-1]),rob1(nums[1:]))