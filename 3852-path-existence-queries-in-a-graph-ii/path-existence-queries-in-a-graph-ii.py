class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        values = [(val, ind) for ind, val in enumerate(nums)]
        index = {}
        values.sort()
        for ind, (a,b) in enumerate(values):
            index[b] = ind
        links = {}
        for ind, (val, _) in enumerate(values):
            n_poss = bisect.bisect_left(values, (val+maxDiff, inf))
            if n_poss<len(values) and values[n_poss][0]<=val+maxDiff:
                links[ind] = n_poss
            else:
                links[ind] = n_poss-1
        ans = []
        @lru_cache(None)
        def dfs(a,b):
            if a>=b: return 0
            if links[a]==a: return -inf
            return 1+dfs(links[a], b)
            
        for a,b in queries:
            res = dfs(min(index[a],index[b]), max(index[a], index[b]))
            ans.append(-1 if res==-inf else res)
        return ans