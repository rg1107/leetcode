class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        N = len(nums)
        dp = [0]* N

        curmax = 0
        dp = [0] * N
        for i in range(N):
            curmax = max(nums[i], curmax)
            dp[i] = curmax
        
        curmin = nums[-1]
        for i in range(N-2, -1, -1):
            if dp[i] > curmin:
                dp[i] = max(dp[i], dp[i+1])
            curmin = min(curmin, nums[i])
        
        return dp
        