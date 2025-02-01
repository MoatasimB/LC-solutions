class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) != self.maxSize:
            self.stack.append([x, 0])


    def pop(self) -> int:
        if not self.stack:
            return - 1
        
        el, increment = self.stack.pop()
        if self.stack:
            self.stack[-1][1] += increment
        
        return el + increment

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        if len(self.stack) <= k:
            self.stack[-1][1] += val
            return
        
        n = len(self.stack)
        index = k - 1

        self.stack[index][1] += val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)