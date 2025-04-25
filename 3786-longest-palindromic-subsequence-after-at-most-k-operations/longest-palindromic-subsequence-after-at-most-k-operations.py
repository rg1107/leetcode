class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        def cost(c1, c2):
            dist = abs(ord(c1) - ord(c2))
            return min(dist, 26-dist)

        # k + 1 because we store 0 to k
        n = len(s)
        dp = [[[0 for _ in range(k+1)] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for kk in range(k+1):
                # single character is palindrome
                dp[i][i][kk] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                for kk in range(k+1):
                    if s[i] == s[j]:
                        dp[i][j][kk] = dp[i+1][j-1][kk] + 2
                    else:
                        dp[i][j][kk] = max(dp[i+1][j][kk], dp[i][j-1][kk])
                        d = cost(s[i], s[j])
                        if d <= kk:
                            dp[i][j][kk] = max(dp[i][j][kk], dp[i+1][j-1][kk-d] + 2)
        
        return dp[0][n-1][k]