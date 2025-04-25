class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
        
        # dp[i][j] represents max sum from j subarrays from i elements
        dp = [[float(-inf)] * (k+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0
        
        for j in range(1, k+1):
            max_prev = float(-inf)
            for i in range(1, n+1):
                if i >=m:
                    max_prev = max(max_prev, dp[i-m][j-1] - pre[i-m])
                    dp[i][j] = max(max_prev + pre[i], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][k]
        