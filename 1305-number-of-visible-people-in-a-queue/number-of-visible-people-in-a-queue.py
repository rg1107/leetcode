class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = [n-1]

        index = n-2

        while index >= 0 and len(stack) != 0:
            while len(stack) > 0 and heights[stack[len(stack) -1]] < heights[index]:
                res[index] += 1
                stack.pop()
            
            if len(stack) > 0:
                res[index] += 1
            
            stack.append(index)
            index -= 1
        
        return res
        