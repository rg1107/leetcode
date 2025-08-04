class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        def find(num, par):
            if par[num] == num:
                return num
            
            par[num] = find(par[num], par)
            return par[num]

        def union(x, y, par):
            parx = find(x, par)
            pary = find(y, par)

            if parx != pary:
                par[pary] = parx
                return parx
            
            return -1

        par = [p for p in range(m*n)]
        nodes = [0 for _ in range(m*n)]
        islands = 0
        res = []

        for pos in positions:
            x, y = pos
            node = x*n + y

            if nodes[node] == 1:
                res.append(islands)
                continue

            vis = set()

            if x - 1 >= 0:
                top = (x-1)*n + y
                if nodes[top] == 1:
                    parent = union(top, node, par)
                    if parent != -1 and (parent not in vis):
                        vis.add(parent)

            if y-1 >= 0:
                left = x*n + y - 1
                if nodes[left] == 1:
                    parent = union(left, node, par)
                    if parent != -1 and (parent not in vis):
                        vis.add(parent)
            
            if y + 1 < n:
                right = x*n + y + 1
                if nodes[right] == 1:
                    parent = union(right, node, par)
                    if parent != -1 and (parent not in vis):
                        vis.add(parent)
            
            if x + 1 < m:
                bottom = (x+1)*n + y
                if nodes[bottom] == 1:
                    parent = union(bottom, node, par)
                    if parent != -1 and (parent not in vis):
                        vis.add(parent)
            
            islands -= (len(vis) - 1)
            nodes[node] = 1
            res.append(islands)
        
        return res

        
        