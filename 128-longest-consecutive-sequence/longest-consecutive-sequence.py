class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen = set()

        for num in nums:
            seen.add(num)

        res = 1

        for num in seen:
            if num + 1 in seen:
                continue
            else:
                cur_len = 0
                temp = num
                while temp in seen:
                    cur_len += 1
                    temp -= 1
                res = max(res, cur_len)
        
        return res
