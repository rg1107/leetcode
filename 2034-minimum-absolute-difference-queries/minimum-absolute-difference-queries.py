class Solution:
    # https://leetcode.com/problems/minimum-absolute-difference-queries/solutions/1284212/python-cumulative-sums-solution-2liner-e-5sga
    def minDifference(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        N, ans, dp = max(nums), [], [[0]*(max(nums)+1)]
        
        for num in nums:
            t = dp[-1][:]
            t[num] += 1
            dp.append(t)

        for a, b in queries:
            diff = [i for x, y, i in zip(dp[b+1], dp[a], range(N+1)) if y != x]
            ans.append(min([b-a for a,b in zip(diff, diff[1:])] or [-1]))
        
        return ans