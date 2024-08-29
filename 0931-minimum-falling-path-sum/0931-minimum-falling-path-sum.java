class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        
        for (int i = n - 2; i >= 0; i--){
            for (int j = n - 1; j >= 0; j--){
                int left = Integer.MAX_VALUE, down = Integer.MAX_VALUE, right = Integer.MAX_VALUE;
                if (j < n -1) right = matrix[i + 1][j + 1];
                if (j > 0) left = matrix[i + 1][j - 1];
                down = matrix[i + 1][j];
                matrix[i][j] += Math.min(left, Math.min(down, right));
            }
        }
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++){
            ans = Math.min(ans, matrix[0][i]);
        }
        return ans;
    }
}