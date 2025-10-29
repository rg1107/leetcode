class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        prev = 0
        count = 1

        for idx in range(len(intervals)):
            if intervals[idx][0] >= intervals[prev][1]:
                prev = idx
                count += 1
        
        return len(intervals) - count