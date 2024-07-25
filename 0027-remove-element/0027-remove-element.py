class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ###Time O(n)  Space O(1)
        pos = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        return pos
    
        
        
        
        l,r=0,0
        count=0
        for r in range(len(nums)):
            if nums[r]!=val:
                nums[l]=nums[r]
                l+=1
            if nums[r]==val:
                count+=1
        return len(nums)-count
