class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stack = []
        self.lastFalse = -1

    def consec(self, num: int) -> bool:
        # print(self.stack, self.lastFalse)
        # if len(self.stack) + 1 < self.k:
        #     self.stack
        #     return False
        
        if num != self.value:
            self.lastFalse = len(self.stack)
        
        self.stack.append(num)
        if len(self.stack) < self.k:
            return False
        if len(self.stack) - self.k > self.lastFalse:
            return True
        
        return False
        
# lf = -1
# [4 4]

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)