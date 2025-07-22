class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        # https://leetcode.com/problems/maximum-weighted-k-edge-path/solutions/6731226/dp-tabulation
        adj = [[] for _ in range(n)]
        for u, v, wt in edges:
            adj[u].append((v, wt))
        
        dp = [[set() for _ in range(k + 1)] for _ in range(n)]

        for u in range(n):
            dp[u][0].add(0)
        
        for e in range(k):
            for u in range(n):
                for v, wt in adj[u]:
                    for w in dp[u][e]:
                        new_wt = w + wt
                        if new_wt < t:
                            dp[v][e+1].add(new_wt)
        
        ans = -1
        for u in range(n):
            if dp[u][k]:
                ans = max(ans, max(dp[u][k]))
        
        return ans


        # graph = defaultdict(list)

        # for edge in edges:
        #     src, dest, wt = edge

        #     if src not in graph:
        #         graph[src] = []

        #     graph[src].append((dest, wt))

        
        # def bfs(graph, start, k, t):
        #     q = deque()
        #     q.append([start, 0])
        #     level = 0
        #     mx = -1

        #     while len(q) > 0:
        #         n = len(q)
        #         if level != k:
        #             for _ in range(n):
        #                 dest, tot = q.popleft()

        #                 for adj in graph[dest]:
        #                     q.append([adj[0], adj[1] + tot])
        #             level += 1
        #         else:
        #             while len(q) > 0:
        #                 ans = q.popleft()
        #                 if ans[1] < t:
        #                     mx = max(mx, ans[1])
            
        #     return mx
        

        # res = -1
        # for index in range(n):
        #     res = max(res, bfs(graph, index, k, t))
        
        # return res
                        
                