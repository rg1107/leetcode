class Solution:
    # https://leetcode.com/problems/largest-rectangle-in-histogram/solutions/688492/python-monotone-increasing-stack-similar-problems-attached
    def largestRectangleArea(self, heights: List[int]) -> int:
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
        