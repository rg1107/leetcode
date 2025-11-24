class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        graph = self._construct_graph(edges)
        dist = self.dijkstra(graph, 0, n)

        min_time = float("-inf")
        print(dist)

        for idx, wait in enumerate(patience):
            m_time = dist[idx] * 2
            
            if wait >= m_time:
                min_time = max(min_time, m_time)
            else:
                mod = m_time % wait
                last = m_time
                if mod == 0:
                    last -= wait
                else:
                    last -= mod

                min_time = max(min_time, last + m_time)
        
        return min_time + 1

    def _construct_graph(self, edges) -> dict:
        graph = dict()

        for edge in edges:
            src, dest = edge
            
            if src not in graph:
                graph[src] = []
            
            if dest not in graph:
                graph[dest] = []
            
            graph[src].append([dest, 1])
            graph[dest].append([src, 1])
        
        return graph

    def dijkstra(self, graph, src, n) -> list:
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0

        heap = [(0, src)]
        vis = set()

        while heap:
            curr_dist, node = heapq.heappop(heap)
            
            if node in vis:
                continue
            
            vis.add(node)

            if node in graph:
                for nei, weight in graph[node]:
                    if curr_dist + weight < dist[nei]:
                        dist[nei] = curr_dist + weight
                        heapq.heappush(heap, (dist[nei], nei))
        
        return dist
        