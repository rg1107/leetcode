class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        R, C = len(seats), len(seats[0])
        
        matching = [[-1] * C for _ in range(R)]
        
        def dfs(node, seen):
            r, c = node
            for nr, nc in [[r-1,c-1], [r,c-1],[r,c+1],[r-1,c+1],[r+1,c-1],[r+1,c+1]]: # assume a virtual edge connecting students who can spy
                if 0 <= nr < R and 0 <= nc < C and seen[nr][nc] == False and seats[nr][nc] == '.':
                    seen[nr][nc] = True
                    if matching[nr][nc] == -1 or dfs(matching[nr][nc], seen):
                        matching[nr][nc] = (r,c)
                        return True
            return False
        
        def Hungarian():
            res = 0
            for c in range(0,C,2):
                for r in range(R):
                    if seats[r][c] == '.':
                        seen = [[False] * C for _ in range(R)]
                        if dfs((r,c), seen):
                            res += 1
            return res
        
        res = Hungarian()
                
        count = 0
        for r in range(R):
            for c in range(C):
                if seats[r][c] == '.':
                    count += 1
        return count - res





    # def maxStudents(self, seats: List[List[str]]) -> int:
    #     # https://leetcode.com/problems/maximum-students-taking-exam/solutions/503686/a-simple-tutorial-on-this-bitmasking-problem
    #     m = len(seats)
    #     n = len(seats[0])
    #     validPos = [0]*m

    #     for i in range(m):
    #         for j in range(n):
    #             validPos[i] |= (1 << j) if seats[i][j] == '.' else 0
        
    #     def bit_count(n):
    #         count = 0
    #         while n:
    #             n &= n-1
    #             count += 1
    #         return count

    #     def backtrack(takenRows, currRow):
    #         if currRow == m:
    #             return 0
            
    #         res = 0

    #         for state in range(1 << n):
    #             if (state & validPos[currRow] == state) and (state & (state << 1) == 0):
    #                 if (takenRows << 1) & state == 0 and (state << 1) & takenRows == 0:
    #                     res = max(res, bit_count(state) + backtrack(state, currRow + 1))

    #         return res
        
    #     return backtrack(0, 0)

        