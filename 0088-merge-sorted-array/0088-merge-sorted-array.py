class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        """
        Compare both arrays from last index, whoever is bigger put it at the end of nums1 array. Doing so, we can sort out the 
        largest elements from back
        """
        i, j, k = m - 1, n - 1, (m + n) - 1
        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            
        
        
#         if not nums2:
#             return 
#         if m==0:
#             for i in range(len(nums2)):
#                 nums1[i]=nums2[i]
#             return
#         i,j=m-1,n-1
#         r=len(nums1)-1
#         while j>=0 and i>=0:
#             if nums1[i]<nums2[j]:
#                 nums1[r]=nums2[j]
#                 j-=1
#             elif nums1[i]>=nums2[j]:
#                 nums1[r]=nums1[i]
#                 #nums1[i]=float("-inf")               
#                 i-=1               
#             r-=1
#         if j>=0 and i<0:
#             while j>=0:
#                 nums1[r]=nums2[j]
#                 j-=1
#                 r-=1
                 