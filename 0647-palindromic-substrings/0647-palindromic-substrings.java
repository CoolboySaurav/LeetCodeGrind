class Solution {
    public int countSubstrings(String s) {
        int n = s.length();  // Declare and initialize n
        boolean[][] dp = new boolean[n][n];  // 2D boolean array initialized to false
        int count = 0;  // To count the palindromic substrings
        
        // Traverse the gaps from 0 to n - 1
        for (int gap = 0; gap < n; gap++) {
            for (int i = 0; i < n - gap; i++) {
                int end = i + gap;
                // Single character is always a palindrome
                if (gap == 0) dp[i][end] = true;
                // Check if the two adjacent characters are equal
                else if (gap == 1) dp[i][end] = (s.charAt(i) == s.charAt(end));
                // Check for longer substrings
                else {
                    dp[i][end] = (s.charAt(i) == s.charAt(end)) && dp[i + 1][end - 1];
                }
                // Increment count if dp[i][end] is true
                if (dp[i][end]) count++;
            }
        }
        return count;  // Return the count of palindromic substrings
    }
}
