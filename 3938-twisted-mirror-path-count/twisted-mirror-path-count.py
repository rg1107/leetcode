class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        mod=(10**9)+7
        count=0

        # dp = [[0,0] * n for _ in range(m)]
        # dp[m-1][n-1][0] = 1
        # dp[m-1][n-1][1] = 1

        # for row in range(m-1, -1, -1):
        #     for col in range(n-1, -1, -1):
        #         for d in range(2):
        #             if grid[i][j] == 1:
        #                 if d == 1 and row + 1 < m:
        #                     dp[row][col] = dp[row + 1][col][0]
        #                 elif col + 1 < n:
        #                     dp[row][col] = dp[row][col+1][1]
        #             else:
        #                 dp[row][col] = dp[row + 1][col][0] + row[row][col + 1][1]
        
        # return dp[0][0] % mod

        @cache
        def rec(i,j,d):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            elif grid[i][j]==1:
                if d==1:
                    return rec(i+1,j,0)
                elif d==0:
                    return rec(i,j+1,1)
            else:
                return rec(i+1,j,0)+rec(i,j+1,1)
        count+=rec(0,0,0)
        rec.cache_clear()
        return count%mod