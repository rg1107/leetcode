class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        res = max(heights)

        for idx in range(len(heights)):
            res = max(res, self.helper(heights, idx))
        
        return res

    
    def helper(self, heights, pIdx) -> int:
        peak = heights[pIdx]
        pMax = peak
        res = peak

        for idx in range(pIdx-1, -1, -1):
            res += min(heights[idx], pMax)
            pMax = min(heights[idx], pMax)
        
        pMax = peak
        for idx in range(pIdx+1, len(heights)):
            res += min(heights[idx], pMax)
            pMax = min(heights[idx], pMax)
        
        return res
        