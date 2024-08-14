class Solution {
    public List<List<String>> solveNQueens(int n) {
        char [][] board = new char[n][n];
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                board[i][j] = '.';
            }
        }
        List<List<String>>result = new ArrayList<>();
        int[] upperDiagonal = new int[(2 * n) - 1];
        int[] lowerDiagonal = new int[(2 * n) - 1];
        int[] leftRow = new int[n];
        
        helper(0, board, upperDiagonal, lowerDiagonal, leftRow, result, n);
        return result;
    }
    private List<String> construct(char[][] board, int n){
        List<String> res = new LinkedList < String>();
        
        for (int i = 0; i < n; i++){
            String s = new String(board[i]);
            res.add(s);
        }
        return res;
    }
    
    private void helper(int col, char[][] board, int[] upperDiagonal, int[] lowerDiagonal, int[] leftRow, List<List<String>> result, int n){
        // Base Case
        if (col == n){
            result.add(construct(board, n));
            return;
        }
        
        for (int i = 0; i < n; i++){
            if ((leftRow[i] != 1) && (upperDiagonal[n - 1 + col - i] != 1) && (lowerDiagonal[col + i] != 1)){
                
                // Recording the path
                board[i][col] = 'Q';
                leftRow[i] = 1;
                upperDiagonal[n - 1 + col - i] = 1;
                lowerDiagonal[col + i] = 1;
                helper(col + 1, board, upperDiagonal, lowerDiagonal, leftRow, result, n);
                
                // Backtracking
                board[i][col] = '.';
                leftRow[i] = 0;
                upperDiagonal[n - 1 + col - i] = 0;
                lowerDiagonal[col + i] = 0;

            }
        }
    }
}