class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[0]]

        rows = 2 ** n
        cols = rows

        grid = [[-1 for _ in range(cols)] for _ in range(rows)]

        numStart = 0
        numEnd = rows*cols - 1

        def helper(rowRange, colRange, start, end, grid):
            rx, ry = rowRange
            cx, cy = colRange

            if rx == ry and cx == cy:
                grid[rx][cx] = end
                return
            
            rmid = (rx + ry) // 2
            cmid = (cx + cy) // 2

            rge = end - start + 1
            mul = rge // 4
            q1 = start + mul - 1
            q2 = start + 2*mul - 1
            q3 = start + 3*mul - 1

            helper([rx, rmid], [cmid + 1, cy], start, q1, grid) #Top right
            helper([rmid + 1, ry], [cmid+1, cy], q1 + 1, q2, grid) #Bottom right
            helper([rmid + 1, ry], [cx, cmid], q2 + 1, q3, grid) #Bottom left
            helper([rx, rmid], [cx, cmid], q3 + 1, end, grid) #Top Left
        
        helper([0, rows - 1], [0, cols - 1], numStart, numEnd, grid)
        return grid


        