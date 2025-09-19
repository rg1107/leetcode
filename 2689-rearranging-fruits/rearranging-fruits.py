class Solution:
    # https://leetcode.com/problems/rearranging-fruits/editorial
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = Counter()
        m = float("inf")
        for b1 in basket1:
            freq[b1] += 1
            m = min(m, b1)
        for b2 in basket2:
            freq[b2] -= 1
            m = min(m, b2)

        merge = []
        for k, c in freq.items():
            if c % 2 != 0:
                return -1 #If odd number of fruits of 1 type , impossible to maintain equal in both
            merge.extend([k] * (abs(c) // 2)) # How many of one type can you share


        if not merge:
            return 0
        merge.sort()
        # Either swap directly or swap twice through min element
        return sum(min(2 * m, x) for x in merge[: len(merge) // 2])
        