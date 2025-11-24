class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if len(source) != len(target):
            return -1
        
        if source == target:
            return 0

        graph = dict()
        for src, dest, c in zip(original, changed, cost):
            if src not in graph:
                graph[src] = []
            graph[src].append([dest, c])
        
        node_dist = dict()

        for src in graph:
            node_dist[src] = self.dijkstra(graph, src)
        
        total = 0
        for src, tar in zip(source, target):
            if src == tar:
                continue
            
            if src in node_dist:
                if tar in node_dist[src]:
                    total += node_dist[src][tar]
                else:
                    return -1
            else:
                return -1
        
        return total

        
    def dijkstra(self, graph, src) -> dict:
        dist = dict()
        dist[src] = 0

        heap = [(0, src)]
        vis = set()

        while heap:
            curr, node = heapq.heappop(heap)
            
            if node in vis:
                continue
            
            vis.add(node)

            if node in graph:
                for nei, weight in graph[node]:
                    if nei not in dist:
                        dist[nei] = float("inf")
                    
                    if curr + weight < dist[nei]:
                        dist[nei] = curr + weight
                        heapq.heappush(heap, [dist[nei], nei])
        
        return dist

        