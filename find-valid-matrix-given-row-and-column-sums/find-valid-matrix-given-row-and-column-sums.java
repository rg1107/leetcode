class Solution {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        
        int[][] res = new int[rowSum.length][colSum.length];
        int r = 0;
        int c = 0;
        
        for(int i = 0;i<rowSum.length;i++) {
            Arrays.fill(res[i], 0);
        }
        
        while(r<rowSum.length && c<colSum.length) {
            if(rowSum[r]<=colSum[c]) {
                res[r][c] = rowSum[r];
                colSum[c] -= rowSum[r];
                r++;
            } else if(rowSum[r] > colSum[c]) {
                res[r][c] = colSum[c];
                rowSum[r] -= colSum[c];
                c++;
            }
        }
        
        return res;
        
    }
}