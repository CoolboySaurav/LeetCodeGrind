class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seq=set()
        for num in nums:
            seq.add(num)
        max1=0
        count=0
        for num in nums:
            if (num-1) not in seq:
                start=num
                while num in seq:
                    num+=1
                max1=max(max1,num-start)
        return max1