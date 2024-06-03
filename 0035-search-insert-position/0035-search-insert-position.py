class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l, r = 0, len(nums) - 1
        ans = r + 1
        
        while l <= r:
            mid = (l + r)//2
            
            if nums[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
                    
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # l=0
        # r=len(nums)-1
        # while r>=l:
        #     mid=(r+l)//2
        #     if nums[mid]==target:
        #         return mid
        #     elif nums[mid]<target:
        #         l=mid+1
        #     else:
        #         r=mid-1
        # return r+1    

        
        