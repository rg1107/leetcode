class Solution:
    # https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/solutions/7367518/javacpython-on-soluiton-by-lee215-3d8g
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        su = n * (n + 1) // 2
        if (su + target) % 2 or abs(target) > su:
            return []
        
        L, R = [], []

        for a in range(n, 0, -1):
            if target + a <= a * (a - 1) // 2:
                L.append(-a)
                target += a
            else:
                R.append(a)
                target -= a

        return L + R[::-1]