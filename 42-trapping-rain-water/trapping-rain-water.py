class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        rmax = [ht for ht in height]
        n = len(height)
        lmax = 0

        for idx in range(n-2, -1, -1):
            rmax[idx] = max(rmax[idx], rmax[idx + 1])

        for idx in range(n):
            lmax = max(lmax, height[idx])
            res += (min(lmax, rmax[idx]) - height[idx])
        
        return res