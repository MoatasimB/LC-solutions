class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        
        gaps = []
       
        meetings = [[start, end] for start, end in zip(startTime, endTime)]
        meetings = [[0,0]] + meetings + [[eventTime, eventTime]]

        meetings.sort()
        n = len(meetings)

        start = meetings[0][0]
        end = meetings[0][1]
        gaps.append(start)
        for s, e in meetings[1:]:
            gaps.append(s - end)
            start = s
            end = e
        gaps.append(eventTime - endTime[-1])
        if sum(gaps) == 0:
            return 0


        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], gaps[i])

        suffix = [0] * n

        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], gaps[i + 1])
        

        print(meetings)
        print(gaps)
        print(prefix, suffix)
        ans = max(gaps)
        for i in range(1, n-1):
            start, end = meetings[i]

            # prevStart, prevEnd = meetings[i-1]
            # nextStart, nextEnd = meetings[i+1]

            prevGap = gaps[i]
            nextGap = gaps[i+1]
            currGap = end - start

            ans = max(ans, prevGap + nextGap)

            if prefix[i-1] >= currGap or suffix[i+1] >= currGap:
                ans = max(ans, prevGap + nextGap + currGap)
        
        return ans



        

