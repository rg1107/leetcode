class Solution {
    /**
    https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/solutions/4130630/greedy-in-c-java-python
     */
    public int minArrayLength(int[] nums, int k) {
        final int n = nums.length;
        int r = 0;
        for (int i = 0; i < n;) {
            int j = i;
            long t = 1;
            while (j < n && (t *= nums[j]) <= k) {
                if (nums[j] == 0) return 1;
                j++;
            }
            r++;
            i = Math.max(i + 1, j);
        }
        return r;
    }
}