class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        counts = defaultdict(int)

        for start, end in intervals:
            counts[start] += 1
            counts[end] -= 1
        
        curr = 0
        ans = 0
        for time, count in sorted(counts.items()):
            curr += count
            ans = max(ans, curr)
        
        return ans