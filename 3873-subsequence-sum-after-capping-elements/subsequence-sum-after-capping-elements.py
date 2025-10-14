class Solution:
    def subsequenceSumAfterCapping(self, A: List[int], k: int) -> List[bool]:
        A.sort()
        n = len(A)
        res = [False] * n
        dp = 1
        mask = (1 << k + 1) - 1
        i = 0
        for x in range(1, n + 1):
            while i < n and A[i] <= x:
                dp |= (dp << A[i]) & mask
                i += 1
            v = max(k % x, k - (n - i) * x)
            for j in range(v, k + 1, x):
                if dp & (1 << j):
                    res[x - 1] = True
                    break
        return res