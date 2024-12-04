class Solution {
    /**
    https://leetcode.com/problems/zero-array-transformation-i/solutions/6055578/java-python-brute-force-to-optimal-line-sweep
     */
    public boolean isZeroArray(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] freq = new int[n];

        for (int[] q: queries) {
            freq[q[0]]++;
            if (q[1] + 1 < n) {
                freq[q[1] + 1]--;
            }
        }

        int sum = 0;
        for (int i=0;i<n;i++) {
            sum += freq[i];
            if ( sum < nums[i]) {
                return false;
            }
        }

        return true;
    }
}