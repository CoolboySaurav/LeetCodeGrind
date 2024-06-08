class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        map1=defaultdict()
        res=[]
        
        def perms(nums,res,map1,ans):        
            if len(ans)==len(nums):
                res.append(ans)
                return 
            for i in xrange(len(nums)):
                if nums[i] not in map1:
                    map1[nums[i]]=1
                    perms(nums,res,map1,ans+[nums[i]])
                    del map1[nums[i]]
        perms(nums,res,map1,[])
        return res
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def permutations(nums,res,map1,ans):
        #     if len(res)==len(nums):
        #         ans.append(res[:])
        #         return
        #     for i in range(len(nums)):
        #         if not map1[nums[i]]:
        #             res.append(nums[i])
        #             map1[nums[i]]=1
        #             permutations(nums,res,map1,ans)
        #             res.pop()
        #             map1[nums[i]]=0
        # map1={}
        # for num in nums:
        #     map1[num]=0
        # ans=[]
        # res=[]
        # permutations(nums,res,map1,ans)
        # return ans
