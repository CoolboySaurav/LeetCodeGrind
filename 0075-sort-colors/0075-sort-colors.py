class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=0
        mid=0
        last=len(nums)-1

        while mid<=last:
            if nums[mid]==0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[mid], nums[last] = nums[last], nums[mid]
                last-=1
        return nums
