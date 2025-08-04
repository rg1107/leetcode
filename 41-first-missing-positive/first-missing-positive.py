class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        def rec(nums, ele, idx):
            if ele <= 0 or ele > n:
                return

            if nums[idx] == idx + 1:
                return
            
            if ele > 0 and ele <= len(nums) and nums[ele - 1] == ele:
                return
            
            if nums[idx] < 0:
                nums[idx] = ele
                return
            
            temp = nums[idx]
            nums[idx] = ele
            rec(nums, temp, temp-1)

        for index in range(n):
            if nums[index] <= 0 or nums[index] > n or nums[index] == index + 1:
                continue
            rec(nums, nums[index], nums[index] - 1)
        
        for index in range(n):
            if nums[index] != index + 1:
                return index + 1
        
        return n + 1

            
        