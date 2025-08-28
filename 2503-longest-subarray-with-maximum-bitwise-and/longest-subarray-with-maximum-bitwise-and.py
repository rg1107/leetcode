class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 1
        cand = nums[0]
        prev = nums[0]
        count = 1

        n = len(nums)
        for i in range(1, n):
            if nums[i] == prev:
                count += 1
                continue
            if prev == cand:
                res = max(res, count)
                cand = prev
            elif prev > cand:
                res = count
                cand = prev
            prev = nums[i]
            count = 1
        
        if prev == cand:
            res = max(res, count)
        elif prev > cand:
            res = count
        
        return res