class MedianFinder:

    def __init__(self):
        self.small = [] #max Heap            2 3  5
        self.large = [] #min Heap           4 6 7    


    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num)

        if len(self.large) > len(self.small) + 1:
            x = -heapq.heappop(self.large)
            heapq.heappush(self.small, x)
        
        if self.small and -self.small[0] > self.large[0]:
            x = -heapq.heappop(self.large)
            heapq.heappush(self.small, x)
        
        if len(self.small) > len(self.large):
            x = -heapq.heappop(self.small)
            heapq.heappush(self.large, x)



    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        
        return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


#  s = -3          l = -2 -1 