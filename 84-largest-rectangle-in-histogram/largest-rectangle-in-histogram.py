class Solution:
    # https://leetcode.com/problems/largest-rectangle-in-histogram/solutions/688492/python-monotone-increasing-stack-similar-problems-attached
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]

        ans = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(i)
        heights.pop()
        return ans
        