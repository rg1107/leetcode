class Solution {
    /**
    https://leetcode.com/problems/perfect-squares/solutions/71488/summary-of-4-different-solutions-bfs-dp-static-dp-and-mathematics
     */
    public int numSquares(int n) {
        if (n <=3) {
            return n;
        }
        int[] dp = new int[n+1];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 3;
        dp[4] = 1;
        return minSquare(n, dp);
    }

    private int minSquare(int n, int[] dp) {
        if (dp[n] != -1) {
            return dp[n];
        }
        
        int rt = (int)Math.sqrt(n);
        int min = Integer.MAX_VALUE;
        for (int i = rt; i>=1;i--) {
            min = Math.min(min, 1 + minSquare(n - i*i, dp));
        }

        dp[n] = min;
        return dp[n];
    }
}