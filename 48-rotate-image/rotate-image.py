class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Transpose
        m = len(matrix)
        n = len(matrix[0])

        for row in range(m):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        # Reverse
        for row in range(m):
            matrix[row] = matrix[row][::-1]
        
        

        