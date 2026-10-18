class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = dict()
        currSum = 0
        ans = 0
        mp[0] = 1

        for num in nums:
            currSum += num
            if (currSum - k) in mp:
                ans += mp[currSum - k]
            
            if currSum not in mp:
                mp[currSum] = 0
            
            mp[currSum] += 1
        
        return ans