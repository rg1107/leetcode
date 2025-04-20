class Solution:
    # https://leetcode.com/problems/find-x-value-of-array-ii/solutions/6669392/square-root-decomposition-vs-segment-tree
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        # Solution 1: Sqrt Decomposition
        def rebuild(b):
            l = b * B
            r = min(n, l + B)
            for p in range(k):
                cnt = [0] * k
                cur = p
                for i in range(l, r):
                    cur = (cur * A[i]) % k
                    cnt[cur] += 1
                block_final[b][p] = cur
                block_cnt[b][p] = cnt

        n = len(nums)
        if k == 1:
            return [n - start for _, _, start, _ in queries]
        B = max(1, int((n / k) ** 0.5))
        A = [v % k for v in nums]
        nb = (n + B - 1) // B
        block_cnt = [[[0] * k for _ in range(k)] for _ in range(nb)]
        block_final = [[0] * k for _ in range(nb)]
        for b in range(nb):
            rebuild(b)
            
        res = []
        for idx, val, start, x in queries:
            A[idx] = val % k
            rebuild(idx // B)
            ans = 0
            p = 1
            b0 = start // B
            end = min(n, (b0 + 1) * B)
            for i in range(start, end):
                p = (p * A[i]) % k
                if p == x:
                    ans += 1
            b = b0 + 1
            while b < nb:
                ans += block_cnt[b][p][x]
                p = block_final[b][p]
                b += 1
            res.append(ans)
        return res





        # # Solution 2: Segment Tree
        # def update(idx: int, val: int):
        #     node = size + idx
        #     for p in range(k):
        #         for r in range(k):
        #             seg_cnt[node][p][r] = 0
        #     for p in range(k):
        #         r = (p * val) % k
        #         seg_final[node][p] = r
        #         seg_cnt[node][p][r] = 1
        #     node //= 2
        #     while node:
        #         L, R = node * 2, node * 2 + 1
        #         fL, fR = seg_final[L], seg_final[R]
        #         cL, cR = seg_cnt[L],   seg_cnt[R]
        #         fN, cN = seg_final[node], seg_cnt[node]
        #         for p in range(k):
        #             mid = fL[p]
        #             fN[p] = fR[mid]
        #             row = cN[p]
        #             left_row  = cL[p]
        #             right_row = cR[mid]
        #             for r in range(k):
        #                 row[r] = left_row[r] + right_row[r]
        #         node //= 2

        # def query_suffix(start: int, x: int) -> int:
        #     l, r = start + size, size + n - 1
        #     left_nodes, right_nodes = [], []
        #     while l <= r:
        #         if l & 1:
        #             left_nodes.append(l)
        #             l += 1
        #         if not (r & 1):
        #             right_nodes.append(r)
        #             r -= 1
        #         l //= 2; r //= 2

        #     nodes = left_nodes + right_nodes[::-1]
        #     res_final = list(range(k))
        #     res_cnt = [[0]*k for _ in range(k)]
        #     for node in nodes:
        #         new_final = [0]*k
        #         new_cnt   = [[0]*k for _ in range(k)]
        #         fN = seg_final[node]
        #         cN = seg_cnt[node]
        #         for p in range(k):
        #             old_row = res_cnt[p]
        #             row     = new_cnt[p]
        #             for r_ in range(k):
        #                 row[r_] = old_row[r_]
        #             mid = res_final[p]
        #             cnt_row = cN[mid]
        #             for r_ in range(k):
        #                 row[r_] += cnt_row[r_]
        #             new_final[p] = fN[mid]
        #         res_final = new_final
        #         res_cnt   = new_cnt
        #     return res_cnt[1][x]

        # n = len(nums)
        # if k == 1:
        #     return [n - start for _, _, start, _ in queries]
        # A = [v % k for v in nums]
        # size = 1
        # while size < n:
        #     size <<= 1

        # seg_final = [None] * (2 * size)
        # seg_cnt   = [None] * (2 * size)
        # for i in range(2 * size):
        #     seg_final[i] = list(range(k))
        #     seg_cnt[i]   = [[0] * k for _ in range(k)]

        # # build leaves
        # for i in range(n):
        #     node = size + i
        #     for p in range(k):
        #         r = (p * A[i]) % k
        #         seg_final[node][p] = r
        #         seg_cnt[node][p][r] = 1

        # # build internals
        # for node in range(size - 1, 0, -1):
        #     L, R = node * 2, node * 2 + 1
        #     fL, fR = seg_final[L], seg_final[R]
        #     cL, cR = seg_cnt[L],   seg_cnt[R]
        #     fN, cN = seg_final[node], seg_cnt[node]
        #     for p in range(k):
        #         mid = fL[p]
        #         fN[p] = fR[mid]
        #         # merge counts
        #         row = cN[p]
        #         left_row  = cL[p]
        #         right_row = cR[mid]
        #         for r in range(k):
        #             row[r] = left_row[r] + right_row[r]
        # ans = []
        # for idx, val, start, x in queries:
        #     update(idx, val % k)
        #     ans.append(query_suffix(start, x))
        # return ans
        