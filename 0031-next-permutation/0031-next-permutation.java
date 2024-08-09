import java.util.Arrays;

class Solution {
    public void nextPermutation(int[] nums) {
        int i = -1;
        
        // Step 1: Find the largest index i such that nums[i] < nums[i + 1]
        for (int j = nums.length - 2; j >= 0; j--) {
            if (nums[j] < nums[j + 1]) {
                i = j;
                break;
            }
        }
        
        // If no such index exists, reverse the whole array
        if (i == -1) {
            reverse(nums, 0, nums.length - 1);
            return;
        }
        
        // Step 2: Find the largest index j greater than i such that nums[i] < nums[j]
        int j = nums.length - 1;
        while (nums[j] <= nums[i]) {
            j--;
        }
        
        // Step 3: Swap nums[i] and nums[j]
        swap(nums, i, j);
        
        // Step 4: Reverse the sequence from nums[i + 1] to the end of the array
        reverse(nums, i + 1, nums.length - 1);
    }
    
    // Helper method to swap elements at indices x and y
    private void swap(int[] nums, int x, int y) {
        int temp = nums[x];
        nums[x] = nums[y];
        nums[y] = temp;
    }
    
    // Helper method to reverse elements from start to end indices
    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }
}
