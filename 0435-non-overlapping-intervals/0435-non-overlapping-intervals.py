class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Greedy approach in this problem is regarding which interval to remove! To do so, we will compare sorted intervals in pair, 
        if the second interval start is in between the first interval, then we will remove the one that ends last. Doing so, we 
        made sure that the interval that ends earliest will be less likely to have any overlap with upcoming intervals
        '''
        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(prevEnd, end)
        return count