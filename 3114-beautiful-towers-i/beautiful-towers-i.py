class Solution:
    # https://leetcode.com/problems/beautiful-towers-i/solutions/4082905/brute-force-solution-by-lee215-xsq3
    def maximumSumOfHeights(self, A: List[int]) -> int:
        n = len(A)

        left = [0] * n
        stack = [-1]
        cur = 0

        for idx in range(n):
            while len(stack) > 1 and A[stack[-1]] > A[idx]:
                j = stack.pop()
                cur -= (j - stack[-1]) * A[j]
            cur += (idx - stack[-1]) * A[idx]
            stack.append(idx)
            left[idx] = cur
        
        stack = [n]
        res = cur = 0

        for idx in range(n-1, -1, -1):
            while len(stack) > 1 and A[stack[-1]] > A[idx]:
                j = stack.pop()
                cur -= -(j - stack[-1]) * A[j]
            cur += -(idx - stack[-1]) * A[idx]
            stack.append(idx)
            res = max(res, left[idx] + cur - A[idx])
        
        return res


    # def maximumSumOfHeights(self, heights: List[int]) -> int:
    #     res = max(heights)

    #     for idx in range(len(heights)):
    #         res = max(res, self.helper(heights, idx))
        
    #     return res

    
    # def helper(self, heights, pIdx) -> int:
    #     peak = heights[pIdx]
    #     pMax = peak
    #     res = peak

    #     for idx in range(pIdx-1, -1, -1):
    #         res += min(heights[idx], pMax)
    #         pMax = min(heights[idx], pMax)
        
    #     pMax = peak
    #     for idx in range(pIdx+1, len(heights)):
    #         res += min(heights[idx], pMax)
    #         pMax = min(heights[idx], pMax)
        
    #     return res
        