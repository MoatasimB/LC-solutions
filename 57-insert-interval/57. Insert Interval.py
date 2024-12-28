class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        s, e = newInterval

        ans = []
        for i, (start, end) in enumerate(intervals):
            if e < start:
                ans.append([s,e])
                return ans + intervals[i:]
            if s > end:
                ans.append(intervals[i])
            elif s <= end:
                s = min(start, s)
                e = max(e, end)
                continue
        
        ans.append([s,e])

        return ans


