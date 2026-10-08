class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        s = sum(chalk)
        k = k % s

        for idx, ch in enumerate(chalk):
            if k < ch:
                return idx
            k = k-ch
        
        return -1
        