class Solution {
    /**
    https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/solutions/4144702/all-scenarios-video-explanation-dp-memo-c-java-python
     */
    // private int[][] dp = new int[501][501];

    // public int minOperations(String s1, String s2, int x) {
    //     int n = s1.length();
    //     int[] v = new int[n];

    //     for (int i = 0; i < n; i++) {
    //         if (s1.charAt(i) != s2.charAt(i)) {
    //             v[i] = i;
    //         }
    //     }

    //     for (int i = 0; i < dp.length; i++) {
    //         Arrays.fill(dp[i], -1);
    //     }

    //     int m = v.length;

    //     if (m % 2 != 0) {
    //         return -1;
    //     }

    //     int ans = solve(0, m - 1, m, v, x);
    //     return ans;
    // }

    // private int solve(int i, int j, int n, int[] v, int x) {
    //     if (i >= n || j < 0 || i > j) {
    //         return 0;
    //     }

    //     if (dp[i][j] != -1) {
    //         return dp[i][j];
    //     }

    //     int a = v[i + 1] - v[i] + solve(i + 2, j, n, v, x);
    //     int b = v[j] - v[j - 1] + solve(i, j - 2, n, v, x);
    //     int c = x + solve(i + 1, j - 1, n, v, x);

    //     dp[i][j] = Math.min(a, Math.min(b, c));
    //     return dp[i][j];
    // }

    public int minOperations(String s1, String s2, int x) {
        int n = s1.length(), res = 0, pre = 1000000, odd = 0;
        for (int i = 0; i < n; i++) {
            pre += 2;
            if (s1.charAt(i) != s2.charAt(i)) {
                int tmp = res;
                res = Math.min(res + x, pre);
                pre = tmp;
                odd ^= 1;
            }
        }
        return odd > 0 ? -1 : res / 2;
    }
}