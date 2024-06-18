class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        maxProfit = -1e7
        left = 0
        for i in range(len(prices)):
            if prices[i] >= prices[left]:
                maxProfit = max(maxProfit, (prices[i]-prices[left]))
            else:
                left = i 
        return maxProfit
        
        
        # maxi=0
        # i,j=0,1
        # profit=0
        # # while j>=0:
        # #     profit=max(profit,0)
        # #     profit-=
        # for p in range(1,len(prices)):
        #     j=p
        #     if prices[j]<prices[i]:
        #         i=p
        #     elif prices[j]>prices[i]:
        #         maxi=max(maxi,prices[j]-prices[i])








        # while i<j:
        #     if prices[j]<prices[i]:
        #         j-=1
        #         continue
        #     elif profit<(prices[j]-prices[i]):
        #         profit=prices[j]-prices[i]
        #         maxi=max(maxi,profit)
        #     i+=1
        #     j-=1
        #return maxi