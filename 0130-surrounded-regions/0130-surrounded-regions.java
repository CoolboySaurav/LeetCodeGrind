class Solution {
    public void solve(char[][] board) {
        int Row = board.length, Col = board[0].length;

        if (Row == 0 || Col == 0) {
            return;
        }

        Queue<Pair<Integer, Integer>> q = new ArrayDeque<>();
        
        // Check the first and last row
        for (int i = 0; i < Col; i++) {
            if (board[0][i] == 'O') {
                q.offer(new Pair<>(0, i));
            }
            if (board[Row - 1][i] == 'O') {
                q.offer(new Pair<>(Row - 1, i));
            }
        }
        
        // Check the first and last column
        for (int i = 0; i < Row; i++) {
            if (board[i][0] == 'O') {
                q.offer(new Pair<>(i, 0));
            }
            if (board[i][Col - 1] == 'O') {
                q.offer(new Pair<>(i, Col - 1));
            }
        }

        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        // Mark all 'O's connected to the borders with a temporary mark '#'
        while (!q.isEmpty()) {
            Pair<Integer, Integer> p = q.poll();
            int row = p.getKey(), col = p.getValue();
            if (board[row][col] == 'O') {
                board[row][col] = '#';  // Mark as visited
                for (int[] d : directions) {
                    int r = row + d[0], c = col + d[1];
                    if (r >= 0 && r < Row && c >= 0 && c < Col && board[r][c] == 'O') {
                        q.offer(new Pair<>(r, c));
                    }
                }
            }
        }

        // Flip all remaining 'O's to 'X', and all '#' back to 'O'
        for (int i = 0; i < Row; i++) {
            for (int j = 0; j < Col; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == '#') {
                    board[i][j] = 'O';
                }
            }
        }
    }
}
