class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int l = findMax(weights), r = sumArray(weights);
        int ans = r;
        while (l <= r){
            int mid = l + (r - l) / 2;
            
            if (possible(weights, mid, days)){
                ans = mid;
                r = mid - 1;
            }
            else l = mid + 1;
        }
        return ans;
    }
    
    private boolean possible(int[] weights, int m, int k){
        int days = 0;
        int total = 0;
        for (int w : weights){
            if (total + w > m) {
                days++;
                total = 0;
            }
            total += w;
        }
        days++;
        return days <= k;
    }
    
    private int sumArray(int[] weights){
        int total = 0;
        for (int w: weights){
            total += w;
        }
        return total;
    }
    
    private int findMax(int[] weights){
        int maxi = Integer.MIN_VALUE;
        
        for (int w : weights){
            maxi = Math.max(maxi, w);
        }
        return maxi;
    }
}