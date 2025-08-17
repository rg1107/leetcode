class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        #https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/solutions/7090815/java-c-python-dp-space-o-k
        dp = [0] + [inf] * k
        res = 0
        for a in nums:
            res += a
            dp[res % k] = min(dp[res % k], res)
            res = dp[res % k]
        return res