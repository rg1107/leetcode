class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        init = [1] * n
        MOD = 10 ** 9 + 7

        for time in range(k):
            for index in range(1, n):
                init[index] = (init[index] + init[index - 1]) % MOD

        # Shorter Math Solution (Pascal Triangle)
        # return comb(k+n-1,n-1) % MOD
        
        return init[n-1]


        