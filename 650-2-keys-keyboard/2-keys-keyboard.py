class Solution:
    def minSteps(self, target: int) -> int:
        if target == 1:
            return 0
        dp = [float('inf')] * (target + 1)

        dp[0] = 0
        dp[1] = 0

        for t in range(2, target + 1):
            for factor in range(1, int(t**0.5) + 1):
                if t % factor == 0:
                    dp[t] = min(dp[t], dp[factor] + t//factor)

                    if factor != t // factor:
                        dp[t] = min(dp[t], dp[t // factor] + factor)
        
        return dp[target]
                