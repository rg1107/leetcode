class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        K = 1024

        dp = [[[0 for k in range(K)] for j in range(n)] for i in range(m)]

        dp[0][0][grid[0][0]] = 1

        for i in range(m):
            for j in range(n):
                for k in range(K):
                    xk = k ^ grid[i][j]
                    if i and dp[i-1][j][xk]:
                        dp[i][j][k] = 1
                    if j and dp[i][j-1][xk]:
                        dp[i][j][k] = 1
        
        ans = 0
        while ans < K:
            if dp[-1][-1][ans]:
                break
            ans += 1
        return ans


    # def minCost(self, grid: list[list[int]]) -> int:
    #     m, n = len(grid), len(grid[0])

    #     heap = [(grid[0][0], 0, 0)]

    #     res = 56054968045

    #     while heap:
    #         xor, x, y = heapq.heappop(heap)

    #         if x == m-1 and y == n-1:
    #             res = min(res, xor)

    #         if x + 1 < m:
    #             heapq.heappush(heap, (xor ^ grid[x + 1][y], x + 1, y))
    #         if y + 1 < n:
    #             heapq.heappush(heap, (xor ^ grid[x][y+1], x, y + 1))

    #     return res
        