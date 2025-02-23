class MyCalendarThree:

    def __init__(self):
        self.meetings = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.meetings[startTime] += 1
        self.meetings[endTime] -= 1

        curr = 0
        ans = 0
        for change in sorted(self.meetings.keys()):
            curr += self.meetings[change]
            ans = max(ans, curr)
        
        return ans