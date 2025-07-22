class Solution:
    def minCost(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/solutions/6483318/python3-10-lines-recursion-t-s-75-60
        @lru_cache(3_000)
        def rec(i, num):
            if i >= n:
                return num
            if i >= n-1:
                return max(nums[i], num)

            lo, md, hi = sorted([num, nums[i], nums[i+1]])

            return min(hi + rec(i + 2, lo), hi + rec(i+2, md), md + rec(i+2, hi))

        n = len(nums)
        return rec(1, nums[0]) 

        