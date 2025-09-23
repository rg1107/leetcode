class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        mod=(10**9)+7
        count=0
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