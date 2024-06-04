class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def findDays(n):
            total = 0
            countDays = 1
            
            for i in weights:
                if total + i <= n:
                    total += i
                else:
                    countDays += 1
                    total = i
            return countDays
        
        l, r = -1e9, 0
        
        for i in weights:
            l = max(l,i)
            r += i
        
        if days == 1:
            return r
        
        while l <= r:
            mid = (l+r)//2
            
            if findDays(mid) > days:
                l = mid + 1
            elif findDays(mid) <= days:
                r = mid - 1

        return l
        
        
        