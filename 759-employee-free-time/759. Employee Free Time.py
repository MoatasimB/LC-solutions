"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        #merge all the intervals of each employe
        def merged(intervals):
            ans = []
            intervals.sort(key = lambda x: x.start)

            ans.append(intervals[0])

            for i in range(1, len(intervals)):
                start = intervals[i].start
                end = intervals[i].end

                if start <= ans[-1].end:
                    ans[-1].end = max(ans[-1].end, end)
                else:
                    ans.append(intervals[i])
            
            return ans

        single = []
        for employeeIntervals in schedule:
            for interval in merged(employeeIntervals):
                single.append(interval)
        

        #merge all the employees with each other now

        ret = merged(single)
        ret.sort(key = lambda x: x.start)

        final = []
        for i in range(1, len(ret)):
            prevInterval = ret[i - 1]
            currInterval = ret[i]

            if prevInterval.end != currInterval.start:
                final.append(Interval(prevInterval.end, currInterval.start))
        
        return final