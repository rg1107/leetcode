class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        count = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    self.dfs(row, col, grid)
                    count += 1

        return count
        
    def dfs(self, x, y, grid):
        if grid[x][y] == '0' or grid[x][y] == '-1':
            return
        
        grid[x][y] = '-1'
        dr = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for direction in dr:
            dx, dy = direction
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '0' and grid[nx][ny] != '-1':
                self.dfs(nx, ny, grid)
