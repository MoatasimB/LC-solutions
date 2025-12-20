class StockPrice:

    def __init__(self):
        self.mpp = {}
        self.maxHeap = []
        self.minHeap = []
        self.currTime = 0
    def update(self, timestamp: int, price: int) -> None:
        self.mpp[timestamp] = price
        heapq.heappush(self.minHeap, [price, timestamp])
        heapq.heappush(self.maxHeap, [-price, timestamp])
        self.currTime = max(self.currTime, timestamp)
    def current(self) -> int:
        return self.mpp[self.currTime]

    def maximum(self) -> int:

        while self.maxHeap and -self.maxHeap[0][0] != self.mpp[self.maxHeap[0][1]]:
            heapq.heappop(self.maxHeap)
        return -self.maxHeap[0][0]

    def minimum(self) -> int:
        #[price, timestamp]
        #check if mpp[timestamp] = price (if it does not this was invalidated)
        while self.minHeap and self.minHeap[0][0] != self.mpp[self.minHeap[0][1]]:
            heapq.heappop(self.minHeap)
        return self.minHeap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()