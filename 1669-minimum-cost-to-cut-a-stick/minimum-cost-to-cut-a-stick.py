class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            return 0 if j - i <= 1 else min(cuts[j] - cuts[i] + dp(i, k) + dp(k, j) for k in range(i+1, j))  
                                                           
        cuts.extend([0, n]); cuts.sort()        
        return dp(0, len(cuts)-1)


        # cuts = sorted(cuts + [0,n])
        # dp = [[0] * len(cuts) for _ in range(len(cuts))]

        # def helper(start: int, end: int, arr: List[int]):
        #     if start >= end:
        #         return 0
            
        #     if not dp[start][end]:
        #         dp[start][end] = 2000000000
        #         for idx in range(start+1, end):
        #             dp[start][end] = min(dp[start][end], arr[end] - arr[start] + helper(start, idx, arr) + helper(idx, end, arr))
            
        #     return dp[start][end]

            # mx = 0
            # cost = end - start
            # for idx, cut in enumerate(arr):
            #     mx = max(mx, cost + helper(start, cut, arr[:idx]) + helper(cut, end, arr[idx+1:]))
            
            # return mx
        
        return helper(0, len(cuts)-1, cuts)

        