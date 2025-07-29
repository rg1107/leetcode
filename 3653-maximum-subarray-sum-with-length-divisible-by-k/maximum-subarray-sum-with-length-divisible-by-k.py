class Solution:
    # Kadane Algo Application
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        mx = -sys.maxsize - 1

        curSum = 0
        for index in range(n):
            prevSum = 0
            if index >= k:
                curSum -= nums[index - k]
                prevSum = dp[index-k]
            
            curSum += nums[index]

            if index + 1 >= k:
                dp[index] = max(curSum, curSum + prevSum)
                mx = max(mx, dp[index])
        
        return mx

        
        # for index in range(n):
        #     dp[index] = nums[index]
        #     if k == 1:
        #         mx = max(mx, dp[index])

        
        # for index in range(n-1):
        #     for jIndex in range(index + 1, n):
        #         dp[index] += nums[jIndex]
        #         if (jIndex - index + 1) % k == 0:
        #             mx = max(mx, dp[index])

        # return mx
        