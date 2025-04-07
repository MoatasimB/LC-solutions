class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.removed = set()
        self.idx = 0

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, [-x, -self.idx])
        self.stack.append([x, self.idx])
        self.idx += 1


    def pop(self) -> int:
        while self.stack and (self.stack[-1][1]) in self.removed:
            self.stack.pop()
        removed_idx = self.stack[-1][1]
        self.removed.add(removed_idx)
        return self.stack.pop()[0]

    def top(self) -> int:
        while self.stack and (self.stack[-1][1]) in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]
    
    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        removed_idx = -self.heap[0][1]
        self.removed.add(removed_idx)
        return -heapq.heappop(self.heap)[0]


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()