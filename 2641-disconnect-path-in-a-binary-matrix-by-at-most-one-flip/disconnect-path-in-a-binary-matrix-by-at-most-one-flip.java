class Solution {
    public boolean isPossibleToCutPath(int[][] grid) {
    int m = grid.length, n = grid[0].length;
    // Initial pruning
    // Forward checking
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            if (i == 0 && j == 0 || grid[i][j] == 0) continue;
            if ((i == 0 || grid[i-1][j] == 0) && (j == 0 || grid[i][j-1] == 0)){
                grid[i][j] = 0;
            }
        }
    }

    // Backwards checking
    for (int i = m-1; i >= 0; i--){
        for (int j = n-1; j >= 0; j--){
            if (i == m-1 && j == n-1 || grid[i][j] == 0) continue;
            if ((i == m-1 || grid[i+1][j] == 0) && (j == n-1 || grid[i][j+1] == 0)){
                grid[i][j] = 0;
            }
        }
    }

    // Diagonal counting
    int[] diagonal = new int[m+n-1];
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            if (grid[i][j] == 1) diagonal[i+j]++;
        }
    }

    // Final count check
    for (int i = 1; i < m+n-2; i++){ 
        if (diagonal[i] < 2) return true;
    }
    return false;
    }
}