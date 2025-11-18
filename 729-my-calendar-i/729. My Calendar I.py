class MyCalendar:

    def __init__(self):
        self.meetings = SortedList() #keep this sorted
        

    def book(self, startTime: int, endTime: int) -> bool:
        l = 0
        r = len(self.meetings) - 1

        while l <= r:
            mid = (l + r) // 2

            s, e = self.meetings[mid]

            if s < startTime:
                l = mid + 1
            else:
                r = mid - 1

        #r + 1 = where our interval should be inserted

        #now we just check if there is no overlap
        idx = r + 1

        if idx > 0 and self.meetings[idx - 1][1] > startTime:
            return False
        if idx < len(self.meetings) and self.meetings[idx][0] < endTime:
            return False
        
        self.meetings.add((startTime, endTime))
        return True


    #      [starTime, endTime] 
    # [s,e]                   [s,e]
        # 2

        [42,49]     #r.    #r + 1
    #    [25,32] [33,41] [47, 50]

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)