class Solution:
    # https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/solutions/6821862/java-c-python-mono-deque-dp
    # def countPartitions(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     dp = [0 for _ in range(n)]
    #     dp[0] = 1

    #     for index in range(1, n):
    #         dp[index] = dp[index - 1]
    #         mn = nums[index]
    #         mx = nums[index]
    #         j = index - 1

    #         for j in range(index - 1, -1, -1):
    #             mn = min(mn, nums[j])
    #             mx = max(mx, nums[j])

    #             if (mx - mn <= k):
    #                 if j != 0:
    #                     dp[index] = (dp[index] + dp[j-1]) % 1000000007
    #                 else:
    #                     dp[index] = (dp[index] + 1) % 1000000007
    #             else:
    #                 break
        
    #     return dp[n-1]
    
    def countPartitions(self, A: List[int], k: int) -> int:
        n = len(A)
        mod = 10**9 + 7
        dp = [1] + [0] * n
        acc = 1
        minq = deque()
        maxq = deque()
        i = 0
        for j in range(n):
            while maxq and A[j] > A[maxq[-1]]:
                maxq.pop()
            maxq.append(j)
            while minq and A[j] < A[minq[-1]]:
                minq.pop()
            minq.append(j)

            while A[maxq[0]] - A[minq[0]] > k:
                acc = (acc - dp[i]) % mod
                i += 1
                if minq[0] < i:
                    minq.popleft()
                if maxq[0] < i:
                    maxq.popleft()
            dp[j + 1] = acc
            acc = (acc + dp[j + 1]) % mod
        return dp[n]

        