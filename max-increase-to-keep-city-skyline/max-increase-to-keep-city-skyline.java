class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        
        int n = grid[0].length;
        
        int[] r = new int[n];
        int[] c = new int[n];
        
        Arrays.fill(r,0);
        Arrays.fill(c,0);
        
        for(int i = 0;i<n;i++){
            for(int j = 0;j<n;j++){
                r[i] = Math.max(r[i], grid[i][j]);
                c[j] = Math.max(c[j], grid[i][j]);
            }
        }
        
        int sum = 0;
        int temp;
        
        for(int i = 0;i<n;i++){
            for(int j = 0;j<n;j++){
                temp = Math.min(r[i], c[j]);
                if(grid[i][j]<temp) {
                    sum += temp-grid[i][j];
                }
            }
        }
        
        return sum;
        
    }
}