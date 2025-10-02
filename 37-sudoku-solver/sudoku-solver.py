class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        res = [[ele for ele in board[idx]] for idx in range(n)]

        for idx in range(n):
            for jIdx in range(n):
                if board[idx][jIdx] != '.':
                    num = int(board[idx][jIdx])
                    rows[idx].add(num)
                    cols[jIdx].add(num)
                    boxes[3*(idx//3) + (jIdx//3)].add(num)

        def solve(x, y) -> bool:
            if x >= n:
                return True

            if y >= n:
                return solve(x + 1, 0)

            
            if board[x][y] != '.':
                return solve(x, y + 1)
            

            if board[x][y] == '.':
                for num in range(1, 10):
                    if num not in rows[x] and num not in cols[y] and num not in boxes[3*(x//3) + (y//3)]:
                        rows[x].add(num)
                        cols[y].add(num)
                        boxes[3*(x//3) + (y//3)].add(num)
                        board[x][y] = str(num)
                        
                        if solve(x, y + 1):
                            return True
                        
                        board[x][y] = '.'
                        rows[x].remove(num)
                        cols[y].remove(num)
                        boxes[3*(x//3) + (y//3)].remove(num)
        
        solve(0, 0)
        


            
