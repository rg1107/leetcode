class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        r -= l
        dp = [1] * (r + 1)
        MOD = 10 ** 9 + 7

        for idx in range(1, n):
            pre = 0

            if idx % 2 == 1:
                for v in range(r + 1):
                    pre2 = pre + dp[v]
                    dp[v] = pre
                    pre = pre2 % MOD
            else:
                for v in range(r, -1, -1):
                    pre2 = pre + dp[v]
                    dp[v] = pre
                    pre = pre2 % MOD
        
        return sum(dp) * 2 % MOD
    
    
    # def zigZagArrays(self, n: int, l: int, r: int) -> int:
    #     MOD = 10 ** 9 + 7
    #     dp = [dict() for _ in range(n)]
    #     for mp in dp:
    #         for num in range(l, r+1):
    #             mp[num] = [0, 0]

    #     for num in range(l, r + 1):
    #         dp[0][num] = [1, 1]
            
    #     for idx in range(1, n):
    #         for num in range(l, r + 1):
    #             for m in range(l, l + (num - l)):
    #                 dp[idx][num][0] = (dp[idx][num][0] + dp[idx - 1][m][1]) % MOD

    #             for m in range(num + 1, r + 1):
    #                 dp[idx][num][1] = (dp[idx][num][1] + dp[idx - 1][m][0]) % MOD

    #     res = 0
    #     for num in range(l, r + 1):
    #         l = dp[n-1][num]
    #         res = (res + l[0]) % MOD
    #         res = (res + l[1]) % MOD

        return res