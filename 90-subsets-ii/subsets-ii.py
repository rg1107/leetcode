class Solution:
    def dfs(self, index, nums, curr, res):
        res.append(curr)

        for j in range(index, len(nums)):
            if j > index and nums[j] == nums[j-1]:
                continue
            self.dfs(j + 1, nums, curr + [nums[j]], res)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(0, nums, [], res)
        return res
        