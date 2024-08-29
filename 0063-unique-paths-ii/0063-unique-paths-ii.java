class Solution {
    public int uniquePathsWithObstacles(int[][] grid){
        int m = grid.length, n = grid[0].length;
                                        
        int[] prev = new int[n];
        
        for (int i = 0; i < m; i++){
            int[] temp = new int[n];
            for (int j = 0; j < n; j++){
                if (grid[i][j] == 1) continue;
                if (i == 0 && j == 0) temp[j] = 1;
                if (i > 0) temp[j] += prev[j];
                if (j > 0) temp[j] += temp[j - 1];
            }
            prev = temp;
        }
        
        return prev[n - 1];
    }
}