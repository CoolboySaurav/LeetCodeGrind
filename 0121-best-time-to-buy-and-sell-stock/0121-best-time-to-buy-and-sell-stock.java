class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = Integer.MIN_VALUE, min_buy = Integer.MAX_VALUE;
        
        for (int i = 0; i < prices.length; i++){
            if (prices[i] < min_buy) min_buy = prices[i];
            maxProfit = Math.max(maxProfit, prices[i] - min_buy);
        } 
        return maxProfit;
    }
}