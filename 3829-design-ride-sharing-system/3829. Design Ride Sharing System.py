class RideSharingSystem:

    def __init__(self):
        self.riders = []
        self.drivers = []
        self.riderIdPeople = {}
        self.t = 0

    def addRider(self, riderId: int) -> None:
        heapq.heappush(self.riders, [self.t, riderId])
        self.riderIdPeople[riderId] = self.t
        self.t += 1
        

    def addDriver(self, driverId: int) -> None:
        heapq.heappush(self.drivers, [self.t, driverId])
        self.t += 1
        

    def matchDriverWithRider(self) -> List[int]:
        while self.riders and self.riders[0][1] not in self.riderIdPeople:
            heapq.heappop(self.riders)
        
        if not self.riders or not self.drivers:
            return [-1, -1]
        
        t, riderId = heapq.heappop(self.riders)
        dt, driverId = heapq.heappop(self.drivers)

        del self.riderIdPeople[riderId]
        return [driverId, riderId]        

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riderIdPeople:
            del self.riderIdPeople[riderId]
        


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)