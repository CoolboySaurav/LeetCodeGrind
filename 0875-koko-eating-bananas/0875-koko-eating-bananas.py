# class Solution(object):
#     def minEatingSpeed(self, piles, h):
#         """
#         :type piles: List[int]
#         :type h: int
#         :rtype: int
#         """
#         max1=0
#         for p in piles:
#             max1=max(max1,p)

#         def totalhours(v,h):
#             totalhour=0
#             for p in v:
#                 totalhour+=math.ceil(p/h)
#             return totalhour
        
#         l=1
#         r=max1
#         m=0
#         while l<=r:
#             m=(l+r)//2
#             # if totalhours(piles,m)<h:
#             #     r=m-1
#             if totalhours(piles,m)<=h:
#                 r=m-1
#             else:
#                 l=m+1
#             # elif totalhours(piles,m)==h:
#             #     l=r=m
#         return l

# class Solution:
#     def minEatingSpeed(self, piles, h):
        
#         l, r = 1, max(piles)
#         res = r
        
#         while l <= r:
#             k = (l+r)//2 
#             totalHours = 0
            
#             for i in piles:
#                 totalHours += math.ceil(i/k)
            
#             if totalHours <= h:
#                 res = min(res, k)
#                 r = k - 1
#             else:
#                 l = k + 1
        
#         return res
                
        
        
        
            
        
        
        
        
class Solution:
    def minEatingSpeed(self, piles, h):
        def check_can_eat(k):
            actual_h = 0
            for pile in piles:
                actual_h += (pile+k-1)//k
            return actual_h <= h
        l,r = 0,max(piles)
        while r-l>1:
            m=(l+r)//2
            if check_can_eat(m):
                r = m
            else:
                l = m
        return r        