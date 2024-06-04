class Solution:
    def search(self, nums: List[int], target: int) -> int:
#         l=0
#         r=len(nums)-1
#         k=0
#         while l<r:
#             mid=(l+r)//2
#             if nums[mid]>nums[r]:
#                 l=mid+1
#             else:
#                 r=mid

#         k=l
#         l=0
#         r=len(nums)-1
#         if target>=nums[k] and target<=nums[r]:
#             l=k
#         else:
#             r=k    
#         #test algo
#         while r>=l:
#             mid=(r+l)//2
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid]<target:
#                 l=mid+1
#             else:
#                 r=mid-1
#         return -1  
        l, r = 0, len(nums)-1
        
        while l<=r:
            mid= (l+r)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l]<= target< nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
