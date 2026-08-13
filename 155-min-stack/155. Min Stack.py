class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        prev = self.stack[-1][1] if self.stack else float("inf")
        min_val = min(prev, value)
        self.stack.append([value, min_val])
        
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()