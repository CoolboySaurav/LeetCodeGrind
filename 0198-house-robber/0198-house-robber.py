class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # Normal Recursion solution with O(2^n) time complexity
        # def testRob(ind):
        #     if ind==0:
        #         return nums[ind]
        #     if ind<0:
        #         return 0
        #     pick=nums[ind]+testRob(ind-2)
        #     notPick=testRob(ind-1)
        #     return max(pick,notPick)
        # return testRob(len(nums)-1)
    
    # Using Memoization to brinf time complexity to O(n) - Top Down Approach
    # Space Complexity of O(n) stack space and O(n) for dp array
        # dp=[-1]*len(nums)
        # def testRob1(ind):
        #     if ind==0:
        #         return nums[ind]
        #     if ind<0:
        #         return 0
        #     if dp[ind]!=-1:
        #         return dp[ind]
        #     pick=nums[ind]+testRob1(ind-2)
        #     notPick=testRob1(ind-1)
        #     dp[ind]=max(pick,notPick)
        #     return dp[ind]
        # return testRob1(len(nums)-1)

    # Tabulation method to reduce the space complexity further-- Bottom Up Approach
        # dp=[0]*len(nums)
        # dp[0]=nums[0]
        
        # for i in range(1,len(nums)):
        #     take=nums[i]
        #     if i>1:
        #         take+=dp[i-2]
        #     notTake=dp[i-1]
        #     dp[i]=max(take,notTake)
        # return dp[len(nums)-1]
    
    # Tabulation method with Space Optimization 
        prev2=0
        prev=nums[0]

        for i in range(1,len(nums)):
            take=nums[i]+prev2
            notTake=prev
            curr=max(take,notTake)
            prev2=prev
            prev=curr
        return prev