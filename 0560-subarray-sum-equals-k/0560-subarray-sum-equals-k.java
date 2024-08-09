import java.util.HashMap;
import java.util.Map;

class Solution {
    public int subarraySum(int[] nums, int k) {
        // Prefix Sum
        Map<Integer, Integer> prefix = new HashMap<>();
        prefix.put(0, 1); // Initialize with sum 0 occurring once
        int curSum = 0, count = 0;
        
        for (int i = 0; i < nums.length; i++) {
            curSum += nums[i];
            int val = curSum - k;
            if (prefix.containsKey(val)) {
                count += prefix.get(val);
            }
            prefix.put(curSum, prefix.getOrDefault(curSum, 0) + 1);
        }
        
        return count;
    }
}
