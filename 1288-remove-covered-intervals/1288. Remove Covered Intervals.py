class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        

        intervals.sort(key = lambda x: (x[0], -x[1]))

        ans = [intervals[0]]

        for x, y in intervals[1:]:
            lastX, lastY = ans[-1]

            if lastY >= y:
                continue
            ans.append([x, y])

        return len(ans)                