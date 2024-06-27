class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # if not nums:
        #     return False
        # elif len(nums)==1:
        #     if nums[0]==target:
        #         return True
        #     else:
        #         return False
        # l=0
        # r=len(nums)-1
        # while l<r:
        #     mid=(l+r)//2
        #     if nums[mid]>nums[r]:
        #         l=mid+1
        #     elif nums[mid]<=nums[r]:
        #         r=mid
        # k=l
        # l = 0
        # r = len(nums) - 1
        # if nums[l] <= target and target <= nums[k-1]:
        #     r = k-1
        # elif nums[k] <= target and target<= nums[r]:
        #     l = k
        
        # while l<r:
        #     mid=(l+r)//2
        #     if nums[mid]<target:
        #         l=mid+1
        #         if nums[l]==target or nums[r]==target:
        #             return True
        #     elif nums[mid]>target:
        #         r=mid
        #         if nums[l]==target or nums[r]==target:
        #             return True
        #     else:
        #         return True
        # return False
        l,r=0,len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target: return True
            
            if nums[l]<nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[l]>nums[mid]:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                l+=1
        return False
            
            
                
        