class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def largestRectangleArea(heights: List[int]) -> int:
            heights.append(0)
            stack = [-1]
            n = len(heights)
            res = 0

            for idx in range(n):
                while heights[idx] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = idx - stack[-1] - 1
                    res = max(res, height * width)
                stack.append(idx)
            stack.pop()
            return res
        

        m = len(matrix)
        n = len(matrix[0])

        temp = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                temp[row][col] = 1 if matrix[row][col] == "1" else 0


        maxArea = largestRectangleArea(temp[0][:])

        for row in range(1, m):
            for col in range(n):
                if temp[row][col] == 1:
                    temp[row][col] += temp[row-1][col]
            
            print(temp[row])

            maxArea = max(maxArea, largestRectangleArea(temp[row][:]))
        
        return maxArea

        