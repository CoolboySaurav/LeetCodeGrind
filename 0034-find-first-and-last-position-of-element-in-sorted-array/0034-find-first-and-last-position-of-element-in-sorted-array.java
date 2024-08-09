import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[]{-1, -1}; // Initialize the result with default values
        
        // Find lower bound
        int l = 0, r = nums.length - 1;
        int lowerBound = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] >= target) {
                if (nums[mid] == target) {
                    lowerBound = mid;
                }
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        
        // If the lower bound is not found, return [-1, -1]
        if (lowerBound == -1) {
            return result;
        }
        
        // Find upper bound
        l = 0;
        r = nums.length - 1;
        int upperBound = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] <= target) {
                if (nums[mid] == target) {
                    upperBound = mid;
                }
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        
        result[0] = lowerBound;
        result[1] = upperBound;
        
        return result;
    }
}
