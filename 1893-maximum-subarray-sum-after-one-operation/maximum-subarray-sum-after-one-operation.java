class Solution {
    public int maxSumAfterOperation(int[] nums) {
        int sum = 0, cur = 0, res = Integer.MIN_VALUE;
        for (int n : nums) {            
            cur = Math.max(n * n, Math.max(cur + n, sum + n * n));
            sum = Math.max(n, sum+n);
            res = Math.max(res, cur);
        }
        return res;
    }
}