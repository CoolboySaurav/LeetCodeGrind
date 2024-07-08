class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        l , r= 0, n - 1
        
        costs = sorted(costs, key = lambda x: (x[1] - x[0]))
        totCost = 0
        
        while l <= r:
            totCost += costs[l][1] + costs[r][0]
            l += 1
            r -= 1
        
        return totCost