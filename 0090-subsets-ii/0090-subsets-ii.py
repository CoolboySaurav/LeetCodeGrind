class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        res=[]
        nums.sort()
        def subset(ind,ds,ans):
            ans.append(ds)            
            for i in xrange(ind,n):
                if i>ind and nums[i]==nums[i-1]:
                    continue
                #ds.append(nums[i])
                subset(i+1,ds+[nums[i]],ans)
                #ds.pop()

        subset(0,[],res)
        return res