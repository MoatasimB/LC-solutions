class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        self.minStack = []
        

    def push(self, val: int) -> None:
        if val <= self.min:
            self.min = val
            self.minStack.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        x = self.stack.pop()

        if x == self.min:
            self.minStack.pop()
        if self.minStack:
            self.min = self.minStack[-1]
        else:
            self.min = float("inf")

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()