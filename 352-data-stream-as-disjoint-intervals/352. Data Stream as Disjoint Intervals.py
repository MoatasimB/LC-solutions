class SummaryRanges:

    def __init__(self):
        self.list = SortedList()
        

    def addNum(self, value: int) -> None:
        if value not in self.list:
            self.list.add(value)
        

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        if len(self.list) == 0:
            return []
        left = right = -1

        for value in self.list:
            if left < 0:
                left = right = value
            elif value == right + 1:
                right = value
            else:
                intervals.append([left, right])
                left = right = value
        intervals.append([left, right])
        return intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()