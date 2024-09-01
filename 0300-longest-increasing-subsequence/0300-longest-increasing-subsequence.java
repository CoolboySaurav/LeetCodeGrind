class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] nxt = new int[n + 1]; // To store the results of subproblems for the next iteration
        int[] cur = new int[n + 1]; // To store the results of subproblems for the current iteration

        for (int i = n - 1; i >= 0; i--) { // Iterate backwards through the array
            for (int j = i - 1; j >= -1; j--) { // Iterate from i-1 down to -1
                int len = nxt[j + 1]; // Option to skip nums[i]
                if (j == -1 || nums[i] > nums[j]) { // Condition to include nums[i] in LIS
                    len = Math.max(len, 1 + nxt[i + 1]); // Update len if including nums[i]
                }
                cur[j + 1] = len; // Store the length in cur for this j
            }
            nxt = cur.clone(); // Copy cur to nxt for the next iteration
        }
        return nxt[0]; // Result is stored in nxt[0] after the loops
    }
}
