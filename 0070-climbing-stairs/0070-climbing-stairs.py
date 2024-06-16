class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Recursion Approach
#         def jump(num):
#             if num<0:
#                 return 0
#             if num == 0:
#                 return 1
            
#             one = jump(num-1)
#             two = jump(num - 2)
            
#             return one + two
        
#         return jump(n)
    
        # Tabulation Approach
        
        dp = [0]*(n+1)
        dp[0] = dp [1] = 1
        
        for i in xrange(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
        
        
        
        
        
        # if n==1:
        #     return 1
        # elif n==2:
        #     return 2
        # prev2=1
        # prev=2
        # curr=0
        # for i in range(2,n):
        #     curr=prev+prev2
        #     prev2=prev
        #     prev=curr
        # return prev