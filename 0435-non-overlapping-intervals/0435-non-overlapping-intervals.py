class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Greedy approach in this problem is regarding which interval to remove! To do so, we will compare sorted intervals in pair, 
        if the second interval start is in between the first interval, then we will remove the one that ends last. Doing so, we 
        made sure that the interval that ends earliest will be less likely to have any overlap with upcoming intervals
        '''
        intervals.sort( key = lambda x : x[0])
        interval = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            a = intervals[i]
            if interval[1] > a[0]: # We have overlap
                count += 1
                if interval[1] > a[1]:
                    interval = a
            else: # No overlap
                interval = a
        return count