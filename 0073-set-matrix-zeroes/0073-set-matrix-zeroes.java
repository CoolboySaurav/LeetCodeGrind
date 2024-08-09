import java.util.HashSet;
import java.util.Set;

class Solution {
    public void setZeroes(int[][] matrix) {
        // Use HashSet for storing row and column indices
        Set<Integer> rows = new HashSet<>();
        Set<Integer> cols = new HashSet<>();
        int R = matrix.length;
        int C = matrix[0].length;
        
        // Identify which rows and columns contain zeroes
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (matrix[i][j] == 0) {
                    rows.add(i);
                    cols.add(j);
                }
            }
        }
        
        // Set the identified rows to zero
        for (int row : rows) {
            for (int j = 0; j < C; j++) {
                matrix[row][j] = 0;
            }
        }
        
        // Set the identified columns to zero
        for (int col : cols) {
            for (int i = 0; i < R; i++) {
                matrix[i][col] = 0;
            }
        }
    }
}
