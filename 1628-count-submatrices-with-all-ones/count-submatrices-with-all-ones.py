class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        for row in range(m):
            for col in range(n):
                if mat[row][col] and row > 0:
                    mat[row][col] += mat[row-1][col]
        

        ans = 0
        for row in range(m):
            stack = []
            cnt = 0

            for col in range(n):
                while stack and mat[row][stack[-1]] > mat[row][col]:
                    topIdx = stack.pop()
                    leftIdx = stack[-1] if stack else -1
                    cnt -= (mat[row][topIdx] - mat[row][col]) * (topIdx - leftIdx)
                
                cnt += mat[row][col]
                ans += cnt
                stack.append(col)
        
        return ans