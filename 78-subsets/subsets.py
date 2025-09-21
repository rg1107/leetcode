class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(idx, nums, curr):
            res.append(curr[:])
            for j in range(idx, len(nums)):
                curr.append(nums[j])
                backtrack(j + 1, nums, curr)
                curr.pop()
        
        backtrack(0, nums, [])
        return res
    
    # def subsetsII(self, nums):
    #     res = []
    #     nums.sort()
    #     self.dfs(nums, 0, [], res)
    #     return res
    
    # def dfs(self, nums, idx, path, res):
    #     res.append(path)
    #     for j in range(idx, len(nums)):
    #         if j > idx and nums[j] == nums[idx]:
    #             continue
    #         self.dfs(nums, j + 1, path + [nums[j]], res)