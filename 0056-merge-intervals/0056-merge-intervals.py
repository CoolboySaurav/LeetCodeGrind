class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        intervals.sort(key=lambda i: i[0])
        res.append(intervals[0])
        if not intervals:
            return intervals
        for i in range(1,len(intervals)):
            if intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
            else:
                a,b=min(res[-1][0],intervals[i][0]),max(res[-1][1],intervals[i][1])
                res[-1]=[a,b]
        return res