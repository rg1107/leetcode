
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [0] * (n + 1)

        # Calculate the first and last gap separately
        gaps[0] = startTime[0]  # Free time before the first meeting
        gaps[n] = eventTime - endTime[-1]  # Free time after the last meeting

        # Compute gaps between meetings
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]

        # Compute prefix sum for efficient range sum calculation
        pref = [0] * (n + 2)
        for i in range(1, n + 2):
            pref[i] = pref[i - 1] + gaps[i - 1]

        # Sliding window to find the maximum sum of k+1 consecutive gaps
        ans = 0
        for i in range(k + 1, n + 2):
            ans = max(ans, pref[i] - pref[i - (k + 1)])

        return ans

        