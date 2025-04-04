class SeatManager:

    def __init__(self, n: int):
        self.min = [i + 1 for i in range(n)]
        

    def reserve(self) -> int:
        x = heapq.heappop(self.min)
        return x
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.min, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)