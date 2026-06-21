class Solution:
    def minOperations(self, nums: list[int]) -> int:
        prevMax = nums[0]
        res = 0

        n = len(nums)
        for idx in range(1, n):
            if nums[idx] < nums[idx - 1]:
                res += (nums[idx-1] - nums[idx])
        
        return res
                
        

        