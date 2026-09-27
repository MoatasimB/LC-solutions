class LogSystem:

    def __init__(self):
        self.lst = SortedList()
        self.mpp = {"Year" : 3,
                    "Month" : 5,
                    "Day" : 7,
                    "Hour" : 9,
                    "Minute" : 11,
                    "Second" : 13          
                    }

    def put(self, id: int, timestamp: str) -> None:
        parts = timestamp.split(":")
        self.lst.add(("".join(parts), id))
        print(self.lst)
        

    def retrieve(self, start: str, end: str, granularity: str) -> list[int]:
        #need to find begin of range
        start = "".join(start.split(":"))
        end = "".join(end.split(":"))
        idx = self.mpp[granularity]
        n = len(self.lst)
        l = 0
        r = n - 1
        startIdx = n
        while l <= r:
            mid = (l + r) // 2

            if self.lst[mid][0][:idx + 1] >= start[:idx + 1]:
                startIdx = mid
                r = mid - 1
            else:
                l = mid + 1
        

        #need to find end of range
        l = 0
        r = n - 1
        endIdx = -1
        while l <= r:
            mid = (l + r) // 2

            if self.lst[mid][0][:idx + 1] <= end[:idx + 1]:
                endIdx = mid
                l = mid + 1
            else:
                r = mid - 1

        print(startIdx, endIdx)
        return [x for _, x in self.lst[startIdx:endIdx + 1]]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)