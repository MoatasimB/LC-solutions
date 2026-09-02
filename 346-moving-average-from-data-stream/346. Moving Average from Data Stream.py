class MovingAverage:

    def __init__(self, size: int):
        self.lst = deque()
        self.size = size
        self.curr = 0

    def next(self, val: int) -> float:
        if len(self.lst) == self.size:
            self.curr -= self.lst.popleft()
        
        self.curr += val
        self.lst.append(val)

        return self.curr / len(self.lst)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)