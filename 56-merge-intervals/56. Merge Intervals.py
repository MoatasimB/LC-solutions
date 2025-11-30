class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x : x[0])

        prevStart = intervals[0][0]
        prevEnd = intervals[0][1]

        ans = []

        for i in range(1, len(intervals)):
            currentStart, currentEnd = intervals[i]

            if currentStart <= prevEnd:
                prevEnd = max(currentEnd, prevEnd)
            elif currentStart > prevEnd:
                ans.append([prevStart, prevEnd])
                prevStart = currentStart
                prevEnd = currentEnd

        ans.append([prevStart, prevEnd])
        return ans                