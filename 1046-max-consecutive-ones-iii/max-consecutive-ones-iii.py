class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        start = 0
        n = len(nums)
        count = 0
        res = 0
        
        for end in range(n):
            if nums[end] == 1:
                count += 1
            
            if end - start + 1 - count > k:
                if nums[start] == 1:
                    count -= 1
                
                start += 1
            
            res = max(res, end - start + 1)
        
        return res
        