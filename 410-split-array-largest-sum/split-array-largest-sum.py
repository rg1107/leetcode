class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)

        def check(nums, k, mid):
            sub = 1
            s = 0
            for index in range(len(nums)):
                s += nums[index]
                if s > mid:
                    sub += 1
                    s = nums[index]
            return sub <= k


        while low < high:
            mid = low + (high - low) // 2

            if check(nums, k, mid):
                high = mid
            else:
                low = mid + 1
        
        return high
        