fmax = lambda x, y: x if x > y else y
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        times = [[0, 0]] + list(zip(startTime, endTime)) + [[eventTime, eventTime]]
        curr = result = 0
        l = 1
        for r in range(1, len(times)):
            curr += times[r][0] - times[r - 1][1]
            while r - l > k:
                curr -= times[l][0] - times[l - 1][1]
                l += 1
            result = fmax(curr, result)
        return result
        
        