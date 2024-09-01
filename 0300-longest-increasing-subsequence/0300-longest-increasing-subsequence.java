class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] lis = new int[n]; // Array to store the length of LIS ending at each index
        int maxLen = 0; // Variable to store the maximum length of LIS
        
        // Initialize the lis array with 1 since the minimum LIS for each element is itself
        for (int i = 0; i < n; i++) {
            lis[i] = 1;
        }
        
        // Iterate backwards through the array
        for (int i = n - 1; i >= 0; i--) {
            // Check every element after the current element i
            for (int j = i + 1; j < n; j++) {
                // If nums[i] < nums[j], then nums[i] can be part of the increasing subsequence ending at j
                if (nums[i] < nums[j]) {
                    lis[i] = Math.max(lis[i], 1 + lis[j]); // Update the LIS ending at i
                }
            }
            maxLen = Math.max(maxLen, lis[i]); // Update the maximum length of LIS found so far
        }
        
        return maxLen; // Return the maximum length of the LIS
    }
}
