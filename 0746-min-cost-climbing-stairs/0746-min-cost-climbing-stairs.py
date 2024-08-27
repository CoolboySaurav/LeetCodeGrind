class Solution:
    def __init__(self):
        self.res = float('inf')
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1])
        
    
        def helper(i, curCost):
            if i >= len(cost):
                self.res = min(self.res, curCost)
                return 
            
            helper(i + 1, curCost + cost[i])
            helper(i + 2, curCost + cost[i])
        
        helper(0, 0)
        helper(1, 0)
        return self.res