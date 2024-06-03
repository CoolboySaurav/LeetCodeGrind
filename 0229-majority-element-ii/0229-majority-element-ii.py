class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def countNum(num):
            count = 0
            for i in nums:
                if num == i:
                    count += 1
            return count
        
        
        
        n = len(nums)
        res = []
        countMap = defaultdict(int)
        
        for i in nums:
            countMap[i] += 1
            if len(countMap)>2:
                for i in countMap.keys():
                    countMap[i] -= 1
        
        for i in countMap.keys():
            if countNum(i) > n/3:
                res.append(i)
        
        return res