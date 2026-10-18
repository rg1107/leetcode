class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        mn = min(nums)
        if mn > k:
            return 0
        
        start = 0
        res = 0
        n = len(nums)
        prd = 1

        for idx in range(n):
            prd *= nums[idx]
            while prd >= k:
                prd /= nums[start]
                start += 1
            res += (idx - start + 1)
        
        return res
        