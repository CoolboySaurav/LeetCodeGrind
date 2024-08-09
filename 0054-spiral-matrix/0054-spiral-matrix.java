import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int R = matrix.length;
        int C = matrix[0].length;
        List<Integer> result = new ArrayList<>();
        
        int l = 0, r = C - 1, u = 0, d = R - 1;
        
        while (l <= r && u <= d) {
            // Traverse from left to right
            for (int i = l; i <= r; i++) {
                result.add(matrix[u][i]);
            }
            u++;
            
            // Traverse from top to bottom
            for (int i = u; i <= d; i++) {
                result.add(matrix[i][r]);
            }
            r--;
            
            // Check if the current boundary is valid
            if (l > r || u > d) {
                break;
            }
            
            // Traverse from right to left
            for (int i = r; i >= l; i--) {
                result.add(matrix[d][i]);
            }
            d--;
            
            // Traverse from bottom to top
            for (int i = d; i >= u; i--) {
                result.add(matrix[i][l]);
            }
            l++;
        }
        
        return result;
    }
}
