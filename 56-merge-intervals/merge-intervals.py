class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        curr = intervals[0]
        n = len(intervals)
        res = []

        for idx in range(1, n):
            ns, ne = intervals[idx]
            s, e = curr
            if ns > e:
                res.append(curr)
                curr = intervals[idx]
            else:
                ns = min(ns, s)
                ne = max(ne,e)
                curr = [ns, ne]
        
        res.append(curr)
        return res

        