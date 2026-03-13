class LogSystem:

    def __init__(self):
        self.logs = SortedList()
        self.gran = {
            "Year": 4,
            "Month": 7,
            "Day":10,
            "Hour":13,
            "Minute":16,
            "Second":19,
        }
        

    def put(self, id: int, timestamp: str) -> None:
        
        self.logs.add([timestamp, id])

        

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        ans = []
        i = self.gran[granularity]

        start = start[:i]
        end = end[:i]

        first = len(self.logs)

        left = 0
        right = len(self.logs) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.logs[mid][0][:i] >= start:
                first = mid
                right = mid - 1
            else:
                left = mid + 1
        
        second = -1

        left = 0
        right = len(self.logs) - 1

        while left <= right:
            mid = (left + right) // 2

            if end >= self.logs[mid][0][:i]:
                second = mid
                left = mid + 1
            else:
                right = mid - 1

        if second < first:
            return []

        return [self.logs[i][1] for i in range(first, second + 1)]

        # return [id for log, id in enumerateself.logs if start <= log[:i] <= end]


        
       



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)