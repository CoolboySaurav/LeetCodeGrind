class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Queue<Pair<Integer, Integer>> q = new ArrayDeque<>();
        int fresh = 0, time = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) fresh++;
                else if (grid[i][j] == 2) q.offer(new Pair<>(i, j));
            }
        }

        int[][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!q.isEmpty() && fresh > 0) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                Pair<Integer, Integer> p = q.poll();
                int row = p.getKey(), col = p.getValue();

                for (int[] d : direction) {
                    int r = row + d[0], c = col + d[1];

                    if (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] == 1) {
                        fresh--;
                        grid[r][c] = 2;
                        q.offer(new Pair<>(r, c));
                    }
                }
            }
            time++;
        }
        return (fresh == 0) ? time : -1;
    }
}
