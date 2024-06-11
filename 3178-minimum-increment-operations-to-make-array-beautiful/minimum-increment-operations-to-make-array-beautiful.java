class Solution {
    /**
    https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/solutions/4220717/java-c-python-dp-o-1-space
     */
    public long minIncrementOperations(int[] A, int k) {
        long dp1 = 0, dp2 = 0, dp3 = 0, dp;
        for (int a: A) {
            dp = Math.min(dp1, Math.min(dp2, dp3)) + Math.max(k - a, 0);
            dp1 = dp2;
            dp2 = dp3;
            dp3 = dp;
        }
        return Math.min(dp1, Math.min(dp2, dp3));
    }
}