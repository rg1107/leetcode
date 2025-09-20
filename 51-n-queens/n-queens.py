class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.'] * n for _ in range(n)]
        rowMap = [False for _ in range(n)]

        res = []

        def isValidPos(row, col, grid):
            if rowMap[row]:
                return False
            x, y = row-1, col-1
            while x >= 0 and y >=0:
                if grid[x][y] == 'Q':
                    return False
                x -= 1
                y -= 1
            
            x, y = row+1, col-1

            while x < len(grid) and y >=0:
                if grid[x][y] == 'Q':
                    return False
                x += 1
                y -= 1
            
            return True

        def rec(col, grid, n):
            if col == n:
                res.append([''.join(s) for s in grid])
                return
            
            for row in range(n):
                if isValidPos(row, col, grid):
                    grid[row][col] = 'Q'
                    rowMap[row] = True
                    rec(col + 1, grid, n)
                    rowMap[row] = False
                    grid[row][col] = '.'
        
        rec(0, grid, n)
        return res



        