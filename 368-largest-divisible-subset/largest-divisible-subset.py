class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        def gcd(m, n):
            if m > n:
                return gcd(n, m)
            
            if m == n or m == 1 or n % m == 0:
                return m
            
            return gcd(n % m, m)

        nums.sort()
        
        n = len(nums)
        dp = [1 for _ in range(n)]
        prev = [-1 for _ in range(n)]

        mx = 1
        mxIdx = 0
        dp[0] = 1

        for idx in range(1, n):
            num = nums[idx]
            for jIdx in range(idx - 1, -1, -1):
                if gcd(nums[jIdx], num) == nums[jIdx]:
                    if dp[jIdx] + 1 > dp[idx]:
                        dp[idx] = dp[jIdx] + 1
                        prev[idx] = jIdx
                        mx = max(mx, dp[idx])
            
            if mx == dp[idx]:
                mxIdx = idx
        
        res = []

        print(nums)
        print(dp)
        print(prev)

        rIdx = mxIdx

        while rIdx != -1:
            res.append(nums[rIdx])
            rIdx = prev[rIdx]
        
        return res

                

        
            

        