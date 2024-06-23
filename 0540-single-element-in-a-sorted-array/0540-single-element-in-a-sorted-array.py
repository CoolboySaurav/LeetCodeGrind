class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        elif nums[0]!=nums[1]:
            return nums[0]
        elif nums[-1]!=nums[-2]:
            return nums[-1]
        l,r=0,len(nums)-1
        while l<=r:
            m=(r-l)//2 +l
            if nums[m-1]<nums[m]<nums[m+1]:
                return nums[m]                
            if (nums[m]!=nums[m+1] and m%2==0) or (nums[m]==nums[m+1] and m%2!=0):
                r=m-1
            elif (nums[m]!=nums[m+1] and m%2!=0) or (nums[m]==nums[m+1] and m%2==0):
                l=m+1