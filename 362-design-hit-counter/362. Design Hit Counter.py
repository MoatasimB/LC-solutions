class HitCounter:

    def __init__(self):
        self.q = deque()
        self.total =0

    def hit(self, timestamp: int) -> None:
        if self.q and timestamp == self.q[-1][1]:
            x = self.q.pop()
            count = x[1]
            t = x[0]
            count +=1
            self.q.append((t,count))
            
        else:
            self.q.append((timestamp, 1))
        
        self.total +=1
    def getHits(self, timestamp: int) -> int:
        while self.q:
            if timestamp - self.q[0][0] >= 300:
                x = self.q.popleft()
                self.total -= x[1]
            else:
                break
        return self.total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)