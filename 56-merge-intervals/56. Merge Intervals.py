class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        final = []
        intervals.sort()

        for i in range(len(intervals)):
            if i == 0:
                final.append(intervals[i])
                continue
            
            start, end = intervals[i]

            if start <= final[-1][1]:
                final[-1][1] = max(final[-1][1], end)
            else:
                final.append(intervals[i])
        
        return final