class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = height[0]
        rmax = [0] * n

        rmax[n-1] = height[n-1]

        for idx in range(n-2, -1, -1):
            rmax[idx] = max(rmax[idx + 1], height[idx])

        res = 0
        for idx in range(n):
            lmax = max(lmax, height[idx])
            res += (min(lmax, rmax[idx]) - height[idx])
        
        return res




        