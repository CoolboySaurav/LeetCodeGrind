class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
         int n = bloomDay.length;
        if (m * k > n) return -1;
        
        int l = findMin(bloomDay), r = findMax(bloomDay);
        int ans = -1;
        
        while (l <= r){
            int mid = l + (r - l) / 2;
            
            if (possible(bloomDay, mid, m, k)){
                ans = mid;
                r = mid - 1;
            }
            else {
                l = mid + 1;
            }
        }
        
        return ans;
    }
    
    private boolean possible(int[] bloomDay, int s, int m, int k){
        int count = 0;
        int numBouquet = 0;
        for (int day : bloomDay){
            if (day <= s){
                count += 1;
            }
            else {
                numBouquet += count / k;
                count = 0;
            }
        }
        numBouquet += count / k;
        return numBouquet >= m;
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
    
    private int findMin(int[] v) {
        int mini = Integer.MAX_VALUE;;
        int n = v.length;
        //find the maximum:
        for (int i = 0; i < n; i++) {
            mini = Math.min(mini, v[i]);
        }
        return mini;
    }

}