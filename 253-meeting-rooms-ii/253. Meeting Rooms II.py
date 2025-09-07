class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        

        intervals.sort(key = lambda x : x[0])


        rooms = []


        rooms.append(intervals[0][1])

        i = 1
        while i < len(intervals):

            if intervals[i][0] >= rooms[0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, intervals[i][1])
            i += 1
        return len(rooms)

