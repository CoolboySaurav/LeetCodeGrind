class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m*k > len(bloomDay):
            return -1
        
        def possible(day):
            numberB = 0
            cnt = 0
            
            for i in bloomDay:
                if i <= day:
                    cnt += 1
                else:
                    numberB += cnt // k
                    cnt = 0
            numberB += cnt//k
            
            return numberB>=m
        
        l,r = min(bloomDay), max(bloomDay)
        ans = -1
        while l <= r:
            mid = (l+r)//2
            
            if possible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
                