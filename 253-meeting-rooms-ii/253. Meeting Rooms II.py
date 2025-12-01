class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        #sweep line algorithm

        meetings = defaultdict(int)

        for start, end in intervals:
            meetings[start] += 1
            meetings[end] -= 1
        
        ans = 0
        curr = 0
        for time, count in sorted(meetings.items()):
            curr += count

            ans = max(ans, curr)
        
        return ans
