class Solution:
    def countPalindromes(self, s: str) -> int:
        mod, n, ans = 10 ** 9 + 7, len(s), 0
        pre, cnts = [[[0] * 10 for _ in range(10)] for _ in range(n)], [0] * 10
        for i in range(n):
            c = ord(s[i]) - ord('0')
            if i:
                for j in range(10):
                    for k in range(10):
                        pre[i][j][k] = pre[i - 1][j][k] 
                        if k == c: pre[i][j][k] += cnts[j]
            cnts[c] += 1
        suf, cnts = [[[0] * 10 for _ in range(10)] for _ in range(n)], [0] * 10
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('0')
            if i < n - 1:
                for j in range(10):
                    for k in range(10):
                        suf[i][j][k] = suf[i + 1][j][k]
                        if k == c: suf[i][j][k] += cnts[j]
            cnts[c] += 1
        for i in range(2, n - 2):
            for j in range(10):
                for k in range(10):
                    ans += pre[i - 1][j][k] * suf[i + 1][j][k]
        return ans % mod
        