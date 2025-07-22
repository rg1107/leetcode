class Solution:
    # https://leetcode.com/problems/closest-equal-element-queries/solutions/6544562/python3-14-lines-bisect-t-s-87-72
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        d, ans = defaultdict(list), []

        for i, num in enumerate(nums):
            d[num].append(i)

        for q in queries:
            idx = d[nums[q]]
            m = len(idx)

            if m == 1: 
                ans.append(-1)
                continue

            j = bisect_left(idx, q)
            mn, mx = sorted([abs(q-idx[j - 1]), abs(q - idx[(j + 1)%m])])
            ans.append(min(mn, n - mx))

        return ans