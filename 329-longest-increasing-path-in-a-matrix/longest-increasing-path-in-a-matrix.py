class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 1

        def dfs(x, y, matrix, dp):
            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
                return 0
            
            if (x, y) in dp:
                return dp[x, y]
            
            dp[x, y] = 1

            dr = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for d in dr:
                dx, dy = d

                nx = x + dx
                ny = y + dy

                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] > matrix[x][y]:
                    dp[x, y] = max(dp[x, y], 1 + dfs(nx, ny, matrix, dp))
            
            return dp[x, y]

        dp = dict()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row, col) not in dp:
                    res = max(res, dfs(row, col, matrix, dp))
        
        return res

        