class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash1={}
        res=[]
        freq=[[] for i in range(len(nums)+1)]
        for n in nums:
            hash1[n]=1+hash1.get(n,0)
        for c,v in hash1.items():
            freq[v].append(c)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        