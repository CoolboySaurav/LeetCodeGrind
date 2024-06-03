class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N= len(nums)
        k = k%N
        
        def reverse(l,r):
            while r>=l:
                nums[l],nums[r]=nums[r],nums[l]
                l += 1
                r -= 1
        
        reverse(0,N-k-1)
        reverse(N-k,N-1)
        reverse(0,N-1)
        
        return
        