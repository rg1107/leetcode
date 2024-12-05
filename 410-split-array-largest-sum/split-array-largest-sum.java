class Solution {
    /**
    https://leetcode.com/problems/split-array-largest-sum/solutions/1084798/java-top-down-recursion-memoization-o-n-2-m-time
     */
    public int splitArray(int[] nums, int m) {
        int[][] memo = new int[nums.length][m+1];
        
        for (int i = 0; i < memo.length; i++) {
            Arrays.fill(memo[i], -1);
        }

        return walk(nums, memo, 0, m);
    }
    
    private int walk(int[] nums, int[][] memo, int start, int rem) { 
	    // base case
        if (rem == 0 && start == nums.length) {
            return 0;
        }
        if (rem == 0 || start == nums.length) {
		    // if we reach the end and have not used up all patitions
			// or have used up all partitions and have not reached the end,
			// we do not want to count the current way of partitioning.
			// Return MAX_VALUE so that we don't contribute to the return value.
            return Integer.MAX_VALUE;
        }
        
        int n = nums.length;
        int ret = Integer.MAX_VALUE;
        int curSum = 0;
        
        if (memo[start][rem] != -1) {
            return memo[start][rem];
        }
        
		// try all positions to end the current partition.
        for (int i = start; i < n; i++) {
            curSum += nums[i];
            
			// answer for partitioning the subarray to the right of the current partition,
			// with one less partition number allowance, because we already used one
			// for the current partition. i.e. (rem - 1).
            int futureSum = walk(nums, memo, i + 1, rem - 1);

            // we want to minimum of the largest sum of the partitions.
            ret = Math.min(ret, Math.max(curSum, futureSum));
        }
        
        memo[start][rem] = ret;
        return ret;
    }
}