class Solution {
    public int uniquePaths(int m, int n) {
        int[] prev = new int[n];
        
        for (int i = 0; i < m; i++) {
            int[] temp = new int[n];
            
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    temp[j] = 1; // Start point
                } 
                if (i > 0) {
                    temp[j] += prev[j]; // Add paths from above
                }
                if (j > 0) {
                    temp[j] += temp[j - 1]; // Add paths from left
                }
            }
            prev = temp; // Copy temp array to prev for the next iteration
        }
        return prev[n - 1];
    }
}
