class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash1 = defaultdict(int)
        
        
        for i in xrange(len(nums)):
            if (target - nums[i]) in hash1:
                return [i,hash1[target - nums[i]]]
            hash1[nums[i]] = i
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         hash1= {}
#         res=[]
#         for i in range(len(nums)):
#             diff=target-nums[i]
#             if diff in hash1:
#                 return [i,hash1[diff]]
                
#             hash1[nums[i]]=i








        # n=len(nums)
        # first=0
        # last=0
        # for i in nums:
        #     first=nums.index(i)
        #     if (first+1==len(nums)-1) and (nums[-1]==(target-i)):
        #         last=len(nums)-1
        #         return[first, last]
        #     else:
        #         new_nums=nums[first+1:]
        #         if (target-i) in new_nums:
        #             last=new_nums.index(target-i)+first+1
        #             return[first,last]
            
