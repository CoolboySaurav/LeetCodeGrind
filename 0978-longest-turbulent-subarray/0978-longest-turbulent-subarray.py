class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        
        # DP Tabulation
        
#         ans = [0]*n
#         ans[0] = 1
#         maxLen = 0
        
#         for i in xrange(1,n-1):
#             if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
#                 ans[i] = ans[i-1] + 1
#             elif arr[i-1] > arr[i] and arr[i] < arr[i+1]:
#                 ans[i] = ans[i-1] + 1
#             else:
#                 ans[i] = 1
#             maxLen = max(maxLen, ans[i])    
            
#         return maxLen
        
        l, r = 0, 1
        res, prev = 1, ""
        
        while r < n:
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r+ 1 if arr[r] == arr[r - 1] else r # r + 1 to adjust l for equality match to skip equal nums sequence else break of pattern can be handled normal way 
                l = r - 1
                prev = ""
        
        return res
                