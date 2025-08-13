class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n1, n2 = len(s), len(p)
        dp = [[False] * (n2+1) for _ in range(n1 + 1)]

        dp[0][0] = True

        for j in range(1, n2+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, n1+1):
            for j in range(1, n2 + 1):
                if s[i-1]==p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False
        return dp[n1][n2]



        # def helper(s, p, i, j):
        #     if i == len(s) and j == len(p):
        #         return True
            
        #     if i >= len(s):
        #         return False
            
        #     if j >= len(p):
        #         return False
            
        #     if p[j].isalpha() and s[i] != p[j]:
        #         return False
            
        #     res = False
        #     if p[j] == '?' or p[j] == s[i]:
        #         res = res or helper(s, p, i+1, j+1)
        #     elif p[j] == '*':
        #         res = res or helper(s, p, i+1, j+1)
        #         res = res or helper(s, p, i+1, j)

        #     return res
        
        # return helper(s, p, 0, 0)
        