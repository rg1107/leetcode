class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vis = [[False] * n for _ in range(m)]

        def dfs(x, y, m, n, grid, vis):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            vis[x][y] = True

            for d in dirs:
                new_x = x + d[0]
                new_y = y + d[1]

                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == "1" and vis[new_x][new_y] == False:
                    vis[new_x][new_y] = True
                    dfs(new_x, new_y, m, n, grid, vis)
        
        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and not vis[row][col]:
                    vis[row][col] = True
                    dfs(row, col ,m, n, grid, vis)
                    res += 1
        
        return res


        