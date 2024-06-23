class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
    
        # Tabulaton Approach
        
        dp = [float('inf')]*(n+1)
        dp[n] = 0
        
        for i in xrange(n-1,-1,-1):
            minJump = float('inf')
            for j in xrange(i + 1, i + nums[i]+1):
                if j <= n:
                    minJump = min(minJump, 1 + dp[j])
            dp[i] = minJump
        
        return dp[0]
    
        #Memoization
        
        dp = [-1]*n
        
        def jump(ind):
            if ind>= n:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            minJump = float('inf')
            for i in range(ind+1, ind+nums[ind]+1):
                minJump = min(minJump, 1 + jump(i))
            dp[ind] = minJump
            return minJump
        
        return jump(0)
        
        #Recursion Approach
        
        def jump(ind):
            if ind>= n:
                return 0
            
            minJump = float('inf')
            for i in range(ind+1, ind+nums[ind]+1):
                minJump = min(minJump, 1 + jump(i))
            return minJump
        
        return jump(0)

    
        