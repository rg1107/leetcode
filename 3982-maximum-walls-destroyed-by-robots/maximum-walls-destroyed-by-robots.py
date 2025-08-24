class Solution:
    # https://leetcode.com/problems/maximum-walls-destroyed-by-robots/solutions/7115549/dp-binary-search
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        def countWalls(left, right):
            if right < left: return 0
            return bisect.bisect_right(walls, right) - bisect.bisect_left(walls, left)

        walls.sort()
        A = [(-inf, 0)] + sorted([(r, d) for r, d in zip(robots, distance)]) + [(inf, 0)]
        dp = [[0, 0] for _ in range(len(robots)+1)]
        
        for i in range(1, len(A)-1):
            r, d = A[i]
            l1, r1, r0 = max(r-d, A[i-1][0]+1), r, min(A[i-1][0]+A[i-1][1], r-1)
            dp[i][0] = max(dp[i-1][0]+countWalls(l1, r1), dp[i-1][1]+countWalls(l1, r1)-countWalls(l1, r0))
            l2, r2 = r, min(r+d, A[i+1][0]-1)
            dp[i][1] = max(dp[i-1]) + countWalls(l2, r2)

        return max(dp[-1])
        