class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # num=count1=count2=0
        # hash1={}
        # for i in range(len(nums)):
        #     if nums[i] not in hash1:
        #         hash1[nums[i]]=1
        #     else:
        #         hash1[nums[i]]+=1
        # max_key = max(hash1, key=lambda k: hash1[k])
        # max_value = hash1[max_key]
        # return max_key
        
        hashSet = defaultdict(int)
        res = majority = 0
        
        for i in nums:
            hashSet[i] += 1
            
            if hashSet[i] > majority:
                majority = hashSet[i]
                res =i
        
        return res
        
        
        
        n = len(nums)
        nums.sort()
        
        return nums[n/2]
        