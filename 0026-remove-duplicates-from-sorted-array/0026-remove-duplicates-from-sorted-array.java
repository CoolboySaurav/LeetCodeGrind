class Solution {
    public int removeDuplicates(int[] nums) {
        // Edge case: if array is empty, return 0
        if (nums.length == 0) {
            return 0;
        }

        // Initialize the `pre` index to 0
        int pre = 0;

        // Iterate over the array starting from the second element
        for (int i = 1; i < nums.length; i++) {
            // If current element is different from the element at `pre` index
            if (nums[i] != nums[pre]) {
                pre++;
                // Move the unique element to the position right after the last unique element
                nums[pre] = nums[i];
            }
        }
        
        // The length of the array with unique elements
        return pre + 1;
    }
}
