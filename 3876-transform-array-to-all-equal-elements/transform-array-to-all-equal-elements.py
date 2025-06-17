class Solution:
    # https://leetcode.com/problems/transform-array-to-all-equal-elements/solutions/6823543/easy-4-lines-with-details
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def check(nums, k, tar):
            arr = nums[:]
            count = 0
            for i in range(len(nums) - 1):
                if arr[i] != tar:
                    arr[i] *= -1
                    arr[i + 1] *= -1
                    count += 1
                    if count > k:
                        return False
            return arr[-1] == tar
        
        return check(nums, k, 1) or check(nums, k, -1)