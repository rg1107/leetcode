class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        n = len(A)
        left, right = [1] * n, [1] * n
        for i in range(1, n):
            if A[i - 1] <= A[i]:
                left[i] = left[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if A[i] <= A[i + 1]:
                right[i] = right[i + 1] + 1

        res = min(n, max(left) + 1)
        for i in range(1, n - 1):
            if A[i - 1] <= A[i + 1]:
                res = max(res, left[i - 1] + 1 + right[i + 1])

        return res