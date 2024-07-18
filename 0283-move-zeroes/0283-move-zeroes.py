class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
                
                
        # j=-1
        # temp=0
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         j=i
        #         break
        # if j==-1:
        #     return nums
        # for i in range(j,len(nums)):
        #     if nums[i]!=0:
        #         nums[j],nums[i]=nums[i],nums[j]
        #         j += 1
        # return nums