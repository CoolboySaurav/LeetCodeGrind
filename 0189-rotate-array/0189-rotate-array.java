class Solution {
    public void rotate(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k == 0) {
            return;
        }

        int N = nums.length;
        k = k % N; // Handle cases where k is greater than N

        // Reverse the entire array
        reverse(nums, 0, N - 1);
        // Reverse the first k elements
        reverse(nums, 0, k - 1);
        // Reverse the rest of the array
        reverse(nums, k, N - 1);
    }

    // Helper method to reverse a portion of the array
    private void reverse(int[] nums, int l, int r) {
        while (l < r) {
            int temp = nums[l]; // Declare temp to hold the value
            nums[l] = nums[r];
            nums[r] = temp;
            l++;
            r--;
        }
    }
}
