class Solution:
    # https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/solutions/6300831/python-combinatorics-explained-o-n-log-n
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        total_sums = 0
        quantity = 1
        
        for i in range(len(nums)):
            total_sums += quantity * (nums[i] + nums[-i - 1])
            quantity = 2 * quantity - comb(i, k - 1)

        return total_sums % (10 ** 9 + 7)
        