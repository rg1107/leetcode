class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(x, y, m, n, board, idx, word) -> bool:
            if idx >= len(word):
                return True

            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[idx]:
                return False

            temp = board[x][y]
            board[x][y] = ''

            dr = [[0, 1], [0,-1], [1, 0], [-1, 0]]

            res = False

            for d in dr:
                new_x = x + d[0]
                new_y = y + d[1]

                res = dfs(new_x, new_y, m, n, board, idx + 1, word)
                if res:
                    return True
                    
            
            board[x][y] = temp
            return False
        
        m = len(board)
        n = len(board[0])

        for idx in range(m):
            for jIdx in range(n):
                res = dfs(idx, jIdx, m, n, board, 0, word)
                if res:
                    return True
        return False



        