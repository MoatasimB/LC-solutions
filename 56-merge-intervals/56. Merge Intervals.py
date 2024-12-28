class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        begin = intervals[0][0]
        prev = intervals[0][1]
        ans = []

        for start, end in intervals:

            if start <= prev:
                prev = max(prev,end)
            elif prev < start:
                ans.append([begin, prev])
                begin = start
                prev = end
        
        ans.append([begin,prev])
        return ans


