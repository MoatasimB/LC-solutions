class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        mpp = defaultdict(int)


        for start, end in intervals:
            mpp[start] += 1
            mpp[end] -= 1
        
        ans = 0
        curr = 0
        for k, v in sorted(mpp.items()):
            curr += v
            ans = max(curr, ans)

        return ans

