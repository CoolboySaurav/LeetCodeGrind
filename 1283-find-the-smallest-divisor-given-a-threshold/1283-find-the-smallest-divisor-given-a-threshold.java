class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int l = 1, r = findMax(nums);
        int ans = r;
        while (l <= r){
            int mid = l + (r - l) / 2;
            
            if (calculate(nums, mid, threshold)){
                ans = mid;
                r = mid - 1;
            }
            else l = mid + 1;
        }
        return ans;
    }
    
    private boolean calculate(int[] nums, int d, int k){
        int total = 0;
        
        for (double num : nums){
            total += (int)Math.ceil(num / d);
        }
        
        return total <= k;
    }
    
    private int findMax(int[] v) {
        int maxi = Integer.MIN_VALUE;;
        int n = v.length;
        //find the maximum:
        for (int i = 0; i < n; i++) {
            maxi = Math.max(maxi, v[i]);
        }
        return maxi;
    }

}