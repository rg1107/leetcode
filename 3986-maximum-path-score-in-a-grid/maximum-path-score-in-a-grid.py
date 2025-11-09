class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # store your requested variable
        quantelis = (grid, k)

        m, n = len(grid), len(grid[0])

        # score and cost lookup
        score_add = {0: 0, 1: 1, 2: 2}
        cost_add  = {0: 0, 1: 1, 2: 1}

        # dp[i][j][c] = max score at cell (i, j) with cost = c
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for cost_used in range(k + 1):

                    if dp[i][j][cost_used] == -1:
                        continue

                    cur_score = dp[i][j][cost_used]

                    # move DOWN
                    if i + 1 < m:
                        nc = cost_used + cost_add[grid[i+1][j]]
                        if nc <= k:
                            ns = cur_score + score_add[grid[i+1][j]]
                            dp[i+1][j][nc] = max(dp[i+1][j][nc], ns)

                    # move RIGHT
                    if j + 1 < n:
                        nc = cost_used + cost_add[grid[i][j+1]]
                        if nc <= k:
                            ns = cur_score + score_add[grid[i][j+1]]
                            dp[i][j+1][nc] = max(dp[i][j+1][nc], ns)

        # result = best score at bottom-right with any cost ≤ k
        best = max(dp[m-1][n-1])
        return best
        
        
        
        
        # m = len(grid)
        # n = len(grid[0])
        # init_cost = 1 if grid[0][0] != 0 else 0
        # init_score = grid[0][0]
        # heap = [(-init_score, init_cost, 0, 0)]

        # while heap:
        #     score, cost, x, y = heapq.heappop(heap)

        #     if cost > k:
        #         continue
            
        #     if x == m - 1 and y == n - 1:
        #         return -score

        #     if x + 1 < m:
        #         cell_cost = 1 if grid[x + 1][y] != 0 else 0
        #         heapq.heappush(heap, (score - grid[x+1][y], cost + cell_cost, x + 1, y))

        #     if y + 1 < n:
        #         cell_cost = 1 if grid[x][y+1] != 0 else 0
        #         heapq.heappush(heap, (score - grid[x][y+1], cost + cell_cost, x, y+1))

        # return -1
        

        
        