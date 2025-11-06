class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0]
        n = len(target)

        for idx in range(1, n):
            res += max(target[idx] - target[idx - 1], 0)

        return res        