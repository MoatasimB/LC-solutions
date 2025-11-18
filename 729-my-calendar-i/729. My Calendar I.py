class MyCalendar:

    def __init__(self):
        self.meetings = [] #keep this sorted
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.meetings:
            self.meetings.append([startTime, endTime])
            return True
        
        firstS, firstE = self.meetings[0]
        if endTime <= firstS:
            self.meetings.insert(0, [startTime, endTime])
            return True

        lastS, lastE = self.meetings[-1]

        if startTime >= lastE:
            self.meetings.append([startTime, endTime])
            return True
        
        flag = False
        for i in range(len(self.meetings) - 1):
            s, e = self.meetings[i]
            nextS, nextE = self.meetings[i + 1]

            if startTime >=e and endTime <= nextS:
                self.meetings.insert(i + 1, [startTime, endTime])
                flag = True
            
            if s > endTime:
                break
        
        return flag

    #      [starTime, endTime] 
    # [s,e]                   [s,e]
        2
    #    [25,32] [33,41] [47, 50]

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)