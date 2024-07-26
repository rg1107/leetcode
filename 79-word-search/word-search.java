class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        boolean[][] vis = new boolean[m][n]; 
        boolean result = false;
        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {
                if(board[i][j] == word.charAt(0)) {
                    vis[i][j] = true;
                    result = dfs(board, vis, i, j, m, n, 1, word);
                    vis[i][j] = false;

                    if (result) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    private void clean(boolean[][] vis) {
        int m = vis.length;
        for (int i =0;i<m;i++) {
            Arrays.fill(vis[i], false);
        }
    }

    private boolean dfs(char[][] board, boolean[][] vis, int i, int j, int m, int n, int k, String word) {
        if (i >=m || i<0 || j>=n || j<0) {
            return false;
        }

        if (k >= word.length()) {
            return true;
        }

        boolean isPossible = false;

        if (i+1<m && !vis[i+1][j] && board[i+1][j] == word.charAt(k)) {
            vis[i+1][j] = true;
            isPossible |= dfs(board, vis, i + 1, j, m, n, k+1, word);
            vis[i+1][j] = false;
        }

        if (i-1>=0 && !vis[i-1][j] && board[i-1][j] == word.charAt(k)) {
            vis[i-1][j] = true;
            isPossible |= dfs(board, vis, i -1, j, m, n, k+1, word);
            vis[i-1][j] = false;
        }

        if (j+1<n && !vis[i][j+1] && board[i][j+1] == word.charAt(k)) {
            vis[i][j+1] = true;
            isPossible |= dfs(board, vis, i, j+1, m, n, k+1, word);
            vis[i][j+1] = false;
        }

        if (j-1>=0 && !vis[i][j-1] && board[i][j-1] == word.charAt(k)) {
            vis[i][j-1] = true;
            isPossible |= dfs(board, vis, i, j-1, m, n, k+1, word);
            vis[i][j-1] = false;
        }

        return isPossible;
    }
}