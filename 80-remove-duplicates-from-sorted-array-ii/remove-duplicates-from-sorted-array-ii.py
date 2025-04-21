class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        map = {}
        index = 0

        for i in range(len(nums)):
            if (nums[i] in map) and map[nums[i]] >= 2:
                continue
            
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] = map[nums[i]] + 1
            nums[i], nums[index] = nums[index], nums[i]
            index += 1

        return index
        