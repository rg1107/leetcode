class Solution {
    /*
    dp[i] = true if we can reach s[i].
    pre means the number of previous position that we can jump from.
    */
    public boolean canReach(String s, int minJ, int maxJ) {
        int n = s.length(), pre = 0;
        boolean[] dp = new boolean[n];
        dp[0] = true;
        for (int i = 1; i < n; ++i) {
            if (i >= minJ && dp[i - minJ])
                pre++;
            if (i > maxJ && dp[i - maxJ - 1])
                pre--;
            dp[i] = pre > 0 && s.charAt(i) == '0';
        }
        return dp[n - 1];
    }
}