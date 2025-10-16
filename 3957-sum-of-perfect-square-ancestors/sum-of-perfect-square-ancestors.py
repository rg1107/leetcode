from collections import defaultdict
from typing import List

class Solution:
    # https://leetcode.com/problems/sum-of-perfect-square-ancestors/solutions/7268245/100-beat-beginner-friendly-explanation-all-languages
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def kernel(x: int) -> int:
            res, f = 1, 2
            while f * f <= x:
                odd = 0
                while x % f == 0:
                    x //= f
                    odd ^= 1
                if odd:
                    res *= f
                f += 1
            if x > 1:
                res *= x
            return res

        k = [kernel(x) for x in nums]
        freq = defaultdict(int)
        ans = 0

        def dfs(u: int, p: int) -> None:
            nonlocal ans
            ans += freq[k[u]]
            freq[k[u]] += 1
            for v in g[u]:
                if v != p:
                    dfs(v, u)
            freq[k[u]] -= 1
            if freq[k[u]] == 0:
                del freq[k[u]]

        dfs(0, -1)
        return ans


# class Solution:
#     def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:

#         if n == 1 or not edges:
#             return 0
        
#         graph = dict()

#         for edge in edges:
#             u, v = edge
#             if u not in graph:
#                 graph[u] = []

#             if v not in graph:
#                 graph[v] = []

#             graph[u].append(v)
#             graph[v].append(u)

#         q = deque()

#         init_state = (0, -1, []) # curr_node, parent, list of ancestors

#         q.append(init_state)
#         res = 0

#         while q:
#             curr_node, par, ancestors = q.popleft()

#             if ancestors:
#                 for anc in ancestors:
#                     if sqrt(nums[curr_node] * nums[anc]) == floor(sqrt(nums[curr_node] * nums[anc])):
#                         res += 1

#             for child in graph[curr_node]:
#                 if child != par:
#                     q.append((child, curr_node, ancestors + [curr_node]))

#         return res
        

