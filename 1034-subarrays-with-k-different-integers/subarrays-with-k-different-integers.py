class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def almostK(nums, k):
            mp = dict()

            start = 0
            res = 0

            for end, num in enumerate(nums):
                if num not in mp:
                    mp[num] = 1
                else:
                    mp[num] += 1

                if len(mp) > k:
                    while len(mp) > k:
                        mp[nums[start]] -= 1
                        if mp[nums[start]] == 0:
                            del mp[nums[start]]
                        start += 1
                res += (end - start + 1)
            
            return res
        
        if k == 1:
            return almostK(nums, k)
        
        return almostK(nums, k) - almostK(nums, k-1)



        