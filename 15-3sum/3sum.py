class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left = 0
        n = len(nums)
        right = n-1

        def findLeft(nums, l, r, t):
            while l < r:
                mid = l + (r-l)//2
                if nums[mid] == t:
                    r = mid
                else:
                    l = mid + 1
            return r
        
        def findRight(nums, l, r, t):
            while l < r:
                mid = l + (r-l)//2
                if nums[mid] == t:
                    l = mid
                else:
                    r = mid - 1
            return l
        
        trip = []
        idx = 0
        for idx in range(n):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            j = idx + 1
            k = n-1
            while j < k:
                total = nums[j] + nums[k] + nums[idx]
                if total == 0:
                    trip.append([nums[idx], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1

                elif total > 0:
                    k -= 1
                else:
                    j += 1
        return trip
            