class Solution {
    public int singleNonDuplicate(int[] nums) {
        int l = 0, r = nums.length - 1;
        
        // Handle edge cases
        if (nums.length == 1) return nums[0];
        if (nums[0] != nums[1]) return nums[0];
        if (nums[r] != nums[r - 1]) return nums[r];
        
        while (l <= r) {
            int mid = l + (r - l) / 2;
            
            // Check if mid is the unique element
            if (mid > 0 && mid < nums.length - 1 && nums[mid] != nums[mid - 1] && nums[mid] != nums[mid + 1]) {
                return nums[mid];
            }
            
            // Check which side to search
            if ((nums[mid] == nums[mid + 1] && mid % 2 == 0) || (nums[mid] != nums[mid + 1] && mid % 2 != 0)) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        
        return -1; // This line is never reached for valid inputs
    }
}
