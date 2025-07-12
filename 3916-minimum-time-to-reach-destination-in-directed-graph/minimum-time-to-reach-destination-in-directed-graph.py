class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        seen = [0] * n
        h = [[0, 0]]
        G = [[] for i in range(n)]

        for u, v, s, e in edges:
            G[u].append([v,s,e])
        
        while h:
            t, u = heappop(h)

            if u == n-1:
                return t
            
            if seen[u]: continue

            seen[u] = 1
            
            for v, s, e in G[u]:
                if t <= e and not seen[v]:
                    heappush(h, [max(t, s) + 1, v])
        
        return -1



            
        
        