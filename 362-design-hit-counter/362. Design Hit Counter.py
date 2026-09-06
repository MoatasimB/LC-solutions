class HitCounter:

    def __init__(self):
        self.lst = deque()
        

    def hit(self, timestamp: int) -> None:
        self.lst.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.lst and self.lst[0] <= timestamp - 300:
            self.lst.popleft()
        
        return len(self.lst)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)