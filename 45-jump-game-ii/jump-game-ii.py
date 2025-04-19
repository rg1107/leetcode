class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        maxIndex = 0
        end = 0

        for index in range(0, len(nums) - 1):
            maxIndex = max(maxIndex, index + nums[index])
            if index == end:
                jump += 1
                end = maxIndex
        
        return jump
        