class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        tot = len(encodedText)
        cols = tot // rows

        grid = [[' '] * cols for row in range(rows)]

        x = 0
        y = 0
        for char in encodedText:
            grid[x][y] = char
            if y == cols - 1:
                x = x + 1
                y = 0
            else:
                y = y + 1
        
        res = ''

        x = 0
        y = 0
        y_base = 0

        while x < rows and y < cols:
            res += grid[x][y]
            if x == rows - 1:
                x = 0
                y = y_base + 1
                y_base = y
                continue
            else:
                x = x + 1
                y = y + 1
        
        return res.rstrip()

        