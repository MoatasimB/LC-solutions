class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0
        self.lastFalse = -1

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.lastFalse = self.count
        
        self.count += 1
        if self.count < self.k:
            return False
        if self.count - self.k > self.lastFalse:
            return True
        
        return False
        
# lf = -1
# [4 4]

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)