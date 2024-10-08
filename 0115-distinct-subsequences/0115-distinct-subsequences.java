import java.util.Arrays;

class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        
        // If t is longer than s, no valid subsequence exists
        if (n > m) {
            return 0;
        }
        
        int [] prev = new int [n + 1];
        prev[0] = 1;
        
        for (int i = 1; i < m + 1; i++){
            int [] cur = new int [n + 1];
            cur[0] = 1;
            for (int j = 1; j < n + 1; j++){
                if (s.charAt(i - 1) == t.charAt(j - 1)){
                    cur[j] = prev[j - 1] + prev[j];
                }
                else{
                    cur[j] = prev[j];
                }
            }
            prev = cur;
        }
        return prev[n];
        
//         int[][] dp = new int[m][n];
//         for (int[] rows : dp) {
//             Arrays.fill(rows, -1);
//         }
        
//         return helper(m - 1, n - 1, s, t, dp);
    }

    private int helper(int i, int j, String s, String t, int[][] dp) {
        if (j < 0) {
            // If t is exhausted, there is exactly one way to match (by taking no characters from s)
            return 1;
        }
        if (i < 0) {
            // If s is exhausted but t is not, there is no way to match
            return 0;
        }
        if (dp[i][j] != -1) {
            // Return already computed result
            return dp[i][j];
        }
        if (s.charAt(i) == t.charAt(j)) {
            // If characters match, choose to include or exclude the character
            dp[i][j] = helper(i - 1, j - 1, s, t, dp) + helper(i - 1, j, s, t, dp);
        } else {
            // If characters don't match, exclude the character from s
            dp[i][j] = helper(i - 1, j, s, t, dp);
        }
        return dp[i][j];
    }
}
