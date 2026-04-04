class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        for num in nums:
            maxOr = maxOr | num
    
        def backtrack(index, currOr):
            if index == len(nums):
                return 1 if currOr == maxOr else 0
            
            include = backtrack(index + 1, currOr | nums[index])
            exclude = backtrack(index + 1, currOr)

            return include + exclude
        
        return backtrack(0, 0)

        