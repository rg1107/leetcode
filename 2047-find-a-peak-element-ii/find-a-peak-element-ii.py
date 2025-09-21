class Solution:
    def maxEl(self, mat, m, n, col):
        maxi = -1
        ind = -1
        for i in range(m):
            if mat[i][col] > maxi:
                maxi = mat[i][col]
                ind = i
        return ind
    
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) //2
            row = self.maxEl(mat, m, n, mid)
            gl = mid - 1 < 0 or mat[row][mid-1] < mat[row][mid]
            gr = mid + 1 > n-1 or mat[row][mid+1] < mat[row][mid]

            if gl and gr:
                return [row, mid]
            elif gl:
                low = mid + 1
            else:
                high = mid - 1

        return [-1, -1]
        