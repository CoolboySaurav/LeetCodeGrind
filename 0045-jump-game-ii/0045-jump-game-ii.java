class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int jump = 0;
        int l = 0, r = 0;

        while (r < n - 1) {  // Updated condition to `r < n - 1`
            int farthest = 0;

            for (int i = l; i <= r; i++) {  // Corrected loop condition to `i <= r`
                farthest = Math.max(farthest, i + nums[i]);
            }
            
            if (farthest == r) { // Edge case: If farthest does not change, it's not possible to proceed.
                return -1;
            }
            
            l = r + 1;
            r = farthest;
            jump++;
        }
        return jump;
    }
}
