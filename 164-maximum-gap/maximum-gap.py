class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        mn, mx = min(nums), max(nums)
        step = max(1, (mx-mn)//(len(nums) - 1))
        size = (mx - mn)//step + 1

        buckets = [[inf, -inf] for _ in range(size)]

        for num in nums:
            i = (num - mn)//step
            left, right = buckets[i]
            buckets[i] = min(left, num), max(right, num)
        
        ans = 0
        prev = mn

        for i in range(size):
            left, right = buckets[i]
            if left < inf:
                ans = max(ans, left - prev)
                prev = right
        
        return ans
        