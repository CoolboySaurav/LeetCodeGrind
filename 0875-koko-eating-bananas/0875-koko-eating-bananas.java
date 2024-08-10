import java.util.Arrays;

class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1; // Minimum possible eating speed
        int r = findMax(piles); // Maximum possible eating speed
        int ans = r;
        while (l <= r) {
            int mid = l + (r - l) / 2; // Middle speed to check
            
            if (canEatAll(piles, mid, h)) {
                ans = mid;
                r = mid - 1; // Try for a smaller speed
            } else {
                l = mid + 1; // Increase speed
            }
        }
        
        return ans;
    }
    
    private boolean canEatAll(int[] piles, int k, int h) {
        int days = 0;
        
        // Calculate total days needed at speed k
        for (double pile : piles) {
            days += Math.ceil(pile / (double)(k));
        }
        
        return days <= h; // Return whether it fits within the allowed hours
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
