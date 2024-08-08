class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxLen = 0;
        int start = 0; // Start at the beginning of the array

        for (int end = 0; end < nums.length; end++) {
            if (nums[end] == 1) {
                // Calculate the length of the current segment of consecutive 1s
                maxLen = Math.max(maxLen, end - start + 1);
            } else {
                // Move start to the next index after the current 0
                start = end + 1;
            }
        }
        
        return maxLen;
    }
}
