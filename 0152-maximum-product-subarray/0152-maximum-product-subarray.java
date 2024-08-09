import java.util.*;

class Solution {
    public int maxProduct(int[] nums) {
        double pre = 1, suff = 1;
        int maxProd = Integer.MIN_VALUE;
        int n = nums.length;
        
        for (int i = 0; i < n; i++){
            if (pre == 0) pre = 1;
            if (suff == 0) suff = 1;
            pre *= nums[i];
            suff *= nums[n - i - 1];
            maxProd = (int)Math.max(maxProd, Math.max(pre, suff));
        }
        return maxProd;
    }
}
