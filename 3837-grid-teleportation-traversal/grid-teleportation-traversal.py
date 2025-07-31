class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        # Missed the question , did not read it correctly, thought that I can teleport only once but question was that I can only use a letter once, changed the whole approach, did not have to use backtracking
        def updateQueue(r: int, c:int) -> None:

            if mat[r][c] == '.':
                queue.append((r,c))
                mat[r][c] = '#'
            
            elif mat[r][c] in teleport:
                queue.extend(teleport[mat[r][c]])
                teleport.pop(mat[r][c])
            
        
        m,n,ans = len(matrix), len(matrix[0]), 0
        mat, queue = list(map(list, matrix)), deque()
        teleport = defaultdict(list)

        dir = ((0,1), (0,-1), (1,0), (-1,0))

        for r, c in product(range(m), range(n)):
            if mat[r][c].isalpha():
                teleport[mat[r][c]].append((r,c))
        
        updateQueue(0,0)

        while queue:

            if (m-1, n-1) in queue: return ans

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in dir:
                    row, col = r + dr, c + dc
                    if 0 <= row < m and 0 <= col < n:
                        updateQueue(row, col)
            
            ans += 1
        
        return -1


                
        