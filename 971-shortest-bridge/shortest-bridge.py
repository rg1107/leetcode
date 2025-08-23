class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        i, j = next((i, j) for i in range(m) for j in range(n) if A[i][j])
        
        # dfs 
        stack = [(i, j)]
        seen = set(stack)
        while stack: 
            i, j = stack.pop()
            seen.add((i, j)) # mark as visited 
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and A[ii][jj] and (ii, jj) not in seen: 
                    stack.append((ii, jj))
                    seen.add((ii, jj))
        
        # bfs 
        ans = 0
        queue = list(seen)
        while queue:
            newq = []
            for i, j in queue: 
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen: 
                        if A[ii][jj] == 1: return ans 
                        newq.append((ii, jj))
                        seen.add((ii, jj))
            queue = newq
            ans += 1
        
        return ans

        # def dfs(grid, x, y, m, n, vis, q):
        #     if x < 0 or y < 0 or x >= m or y >=n:
        #         return
            
        #     vis.add((x,y))

        #     dr = [[0, 1], [1,0], [-1, 0], [0, -1]]

        #     count = 0

        #     for d in dr:
        #         dx, dy = d
        #         nx = x + dx
        #         ny = y + dy
        #         if nx < 0 or ny < 0 or nx >=m or ny >= n or grid[nx][ny] == 1:
        #             count += 1
            
        #     if count < 4:
        #         isCorner = True
        #         q.append((x, y, 0))

        #     for d in dr:
        #         dx, dy = d
        #         nx = x + dx
        #         ny = y + dy

        #         if nx >= 0 and ny >=0 and nx < m and ny < n and grid[nx][ny] == 1 and (nx,ny) not in vis:
        #             dfs(grid, nx, ny, m, n, vis, q)
                
        # vis = set()
        # q = deque()

        # m = len(grid)
        # n = len(grid[0])
        # dfsDone = False

        # for idx in range(m):
        #     for jIdx in range(n):
        #         if grid[idx][jIdx] == 1:
        #             dfs(grid, idx, jIdx, m, n, vis, q)
        #             dfsDone = True
        #             break
            
        #     if dfsDone:
        #         break
        
        # while len(q) > 0:
        #     state = q.popleft()
        #     x, y, dist = state
        #     vis.add((x,y))

        #     dr = [[0, 1], [1,0], [-1, 0], [0, -1]]

        #     for d in dr:
        #         dx, dy = d
        #         nx = x + dx
        #         ny = y + dy
        #         if nx >= 0 and ny >=0 and nx < m and ny < n and (nx,ny) not in vis:
        #             if grid[nx][ny] == 1:
        #                 return dist
        #             else:
        #                 q.append((nx, ny, dist + 1))
        
        # return -1

                    

        