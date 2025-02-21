class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        start, end = intervals[0]
        ans = 0
        for s, e in intervals[1:]:
            if s < end:
                ans += 1
                end = min(e, end)
            else:
                end = e
        
        return ans
