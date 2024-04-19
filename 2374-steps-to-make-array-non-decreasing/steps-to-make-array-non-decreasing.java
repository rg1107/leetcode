class Solution {
    /**
        https://leetcode.com/problems/steps-to-make-array-non-decreasing/solutions/2085864/java-c-python-stack-dp-explanation-poem
     */
    public int totalSteps(int[] nums) {
        int n = nums.length;
        int[] stack = new int[n];
        int[] dp = new int[n];
        int j = -1;
        int res = 0;

        for (int i = n-1; i >=0;i--) {
            while (j >=0 && nums[i] > nums[stack[j]]) {
                dp[i] = Math.max(++dp[i], dp[stack[j--]]);
                res = Math.max(res, dp[i]);
            }
            stack[++j] = i;
        }

        return res;
    }
}