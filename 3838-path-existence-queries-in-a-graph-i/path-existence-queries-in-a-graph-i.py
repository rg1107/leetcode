class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # Nums array is already sorted so giving O(n) for each union Hence Disjoint set is giving TLE

        prev = nums[0]
        nums[0] = 0

        for index in range(1, n):
            if abs(nums[index] - prev) <= maxDiff:
                prev = nums[index]
                nums[index] = nums[index - 1]
            else:
                prev = nums[index]
                nums[index] = index
        
        return [nums[u] == nums[v] for u, v in queries]
        
        # par = [index for index in range(n)]

        # def find(node, par):
        #     if par[node] == node:
        #         return node
        #     par[node] = find(par[node], par)
        #     return par[node]
        
        # def union(x, y, par, query_mode):
        #     parx = find(x, par)
        #     pary = find(y, par)

        #     if parx != pary:
        #         if not query_mode:
        #             par[pary] = parx
        #         return False
            
        #     return True

        # for index in range(1, n):
        #     for jIndex in range(index - 1, -1, -1):
        #         if nums[index] - nums[jIndex] <= maxDiff:
        #             union(index, jIndex, par, False)
        #         else:
        #             break
        
        # res = []
        # for query in queries:
        #     u, v = query
        #     res.append(union(u,v,par,True))
        
        # return res
                    

        