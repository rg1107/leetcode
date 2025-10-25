class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        cnt = Counter(mat[0])
        for row in mat[1:]:
            nxt = Counter()
            for a in row:
                for v, c in cnt.items():
                    nxt[gcd(a, v)] = (nxt[gcd(a, v)] + c) % MOD
            cnt = nxt
        return cnt[1]