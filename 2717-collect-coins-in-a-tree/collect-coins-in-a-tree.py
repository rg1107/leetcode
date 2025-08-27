class Solution:
    # https://leetcode.com/problems/collect-coins-in-a-tree/solutions/3347482/day-361-100-java-c-python-explained-most-upvoted-meme
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        tree = [set() for _ in range(n)]

        for e in edges:
            tree[e[0]].add(e[1])
            tree[e[1]].add(e[0])


        leaf = []

        for i in range(n):
            u = i
            while len(tree[u]) == 1 and coins[u] == 0:
                v = tree[u].pop()
                tree[v].remove(u)
                u = v
            
            if len(tree[u]) == 1:
                leaf.append(u)
        
        for sz in range(2, 0, -1):
            temp = []
            for u in leaf:
                if len(tree[u]) == 1:
                    v = tree[u].pop()
                    tree[v].remove(u)
                    if len(tree[v]) == 1:
                        temp.append(v)
            leaf = temp
        
        ans = 0
        for i in range(n):
            ans += len(tree[i])
        
        return ans
    

    # Another Solution

#     def _build_tree(edges: list[list[int]]) -> list[list[int]]:
#     tree = [[] for _ in range(len(edges) + 1)]

#     for vertex, adjacent in edges:
#         tree[vertex].append(adjacent)
#         tree[adjacent].append(vertex)

#     return tree


# class Solution:
#     def collectTheCoins(self, coins: list[int], edges: list[list[int]]) -> int:
#         tree = _build_tree(edges)
#         degree = list(map(len, tree))

#         queue = collections.deque()

#         for vertex in range(len(tree)):
#             if degree[vertex] == 1:
#                 if coins[vertex]:
#                     queue.append((vertex, True))
#                 else:
#                     queue.appendleft((vertex, True))

#         count_pruned = 0

#         while queue:
#             vertex, is_leaf = queue.popleft()
#             count_pruned += 1

#             for adjacent in tree[vertex]:
#                 degree[adjacent] -= 1

#                 if is_leaf and degree[adjacent] == 1:
#                     if coins[vertex]:
#                         queue.append((adjacent, False))
#                     elif coins[adjacent]:
#                         queue.append((adjacent, True))
#                     else:
#                         queue.appendleft((adjacent, True))

#         return 2 * max(0, len(edges) - count_pruned)
        