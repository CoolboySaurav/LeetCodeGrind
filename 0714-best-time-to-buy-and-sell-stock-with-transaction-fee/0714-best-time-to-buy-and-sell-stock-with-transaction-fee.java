class Solution {
    public int maxProfit(int[] prices, int fee) {
        int n = prices.length;
        int[] nxt = new int[2];
        int[] cur = new int[2];
        
        for (int i = n - 1; i >= 0; i--){
            for (int b = 0; b < 2; b++){
                if (b == 0){
                    cur[b] = Math.max(nxt[0], - prices[i] + nxt[1]);
                }
                else{
                    cur[b] = Math.max(nxt[1], prices[i] - fee + nxt[0]);
                }
            }
            nxt = cur;
        }
        return nxt[0];
    }
}