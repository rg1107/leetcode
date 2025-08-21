class Solution:
    def longestSubarray(self, A: List[int], limit: int) -> int:
        # https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solutions/609771/java-c-python-deques-o-n
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        res = 0
        for j, a in enumerate(A):
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)
            while maxd[0] - mind[0] > limit:
                if maxd[0] == A[i]: maxd.popleft()
                if mind[0] == A[i]: mind.popleft()
                i += 1
            
            res = max(res, j-i + 1)
        return res