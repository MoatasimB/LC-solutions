class StockPrice:

    def __init__(self):
        self.history = {}
        self.last = 0
        self.max = []
        self.min = []

    def update(self, timestamp: int, price: int) -> None:
        self.history[timestamp] = price
        heapq.heappush(self.max, [-price, timestamp])
        heapq.heappush(self.min, [price, timestamp])

        self.last = max(self.last, timestamp)

    def current(self) -> int:
        return self.history[self.last]
        

    def maximum(self) -> int:
        while self.max and -self.max[0][0] != self.history[self.max[0][1]]:
            heapq.heappop(self.max)
        return -self.max[0][0]
    def minimum(self) -> int:
        while self.min and self.min[0][0] != self.history[self.min[0][1]]:
            heapq.heappop(self.min)
        return self.min[0][0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()