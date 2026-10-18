class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        mx_so_far = 0
        mx_ending_here = 0

        all_neg = True
        max_neg = -10**5

        for num in nums:
            if num >= 0:
                all_neg = False
                break
            max_neg = max(max_neg, num)
        
        if all_neg:
            return max_neg


        for num in nums:
            mx_ending_here += num

            if mx_ending_here < 0:
                mx_ending_here = 0

            mx_so_far = max(mx_so_far, mx_ending_here)
        
        return mx_so_far
        