class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        ans = []

        start = newInterval[0]
        end = newInterval[1]

        for i in range(len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if end < s:
                ans.append([start, end])
                return ans + intervals[i:]
            if e < start:
                ans.append(intervals[i])
            else:
                start = min(start, s)
                end = max(end, e)
        
        ans.append([start,end])
        return ans
        






