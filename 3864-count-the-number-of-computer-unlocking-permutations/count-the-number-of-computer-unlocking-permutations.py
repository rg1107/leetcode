class Solution:
    MOD = 10**9 + 7
    def countPermutations(self, comp: List[int]) -> int:
        n = len(comp)
        ans = 1

        for i in range(1, n):
            if comp[i] <= comp[0]:
                return 0
            ans *= i
            ans %= self.MOD

        return ans
        