class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def rec(idx, currSum):
            if idx == n:
                if currSum == target:
                    return 1
                else:
                    return 0
            
            return rec(idx + 1, currSum + nums[idx]) + rec(idx + 1, currSum - nums[idx])
        
        n = len(nums)
        return rec(0, 0)