class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int result = n;
        
        for (int i = 0; i < nums.length; i++){
            result += i - nums[i];
        }
        return result;
    }
}