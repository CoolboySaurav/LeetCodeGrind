class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0]; // Special case: only one house
        
        // Rob excluding the last house and excluding the first house
        return Math.max(helper(nums, 0, n - 2), helper(nums, 1, n - 1));
    }
    
    private int helper(int[] nums, int start, int end) {
        int prev2 = 0; // Equivalent to the value two houses back
        int prev = 0;  // Equivalent to the value one house back
        
        for (int i = start; i <= end; i++) {
            // Rob current house and add to prev2 (skip one house) or skip current (prev)
            int cur = Math.max(nums[i] + prev2, prev);
            prev2 = prev; // Update prev2 to be the previous house's value
            prev = cur;   // Update prev to be the current house's value
        }
        return prev;
    }
}
