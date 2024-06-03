class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l=0
        r=len(nums)-1
        mid=0
        ans1=ans2=-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] >= target:
                r = mid - 1
                if nums[mid] == target:
                    ans2 = mid

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
                if nums[mid] == target:
                    ans1 = mid
            else:
                r = mid - 1
        
        if  ans1!=-1 and ans2!=-1:
            return [ans2,ans1]
        else:
            return [-1,-1]
        