class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        q1=collections.deque()
        q2=collections.deque()
        for num in nums:
            if num<0:
                q1.append(num)
            else:
                q2.append(num)
        i=0
        if q1 or q2:
            while q1 or q2:
                nums[i]=q2.popleft()
                i+=1
                nums[i]=q1.popleft()
                i+=1
        return nums