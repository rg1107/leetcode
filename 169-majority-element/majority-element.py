class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = nums[0]
        cnt = 0

        for index in range(len(nums)):
            if nums[index] == cand:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt <= 0:
                cand = nums[index]
                cnt = 1
        
        return cand


        