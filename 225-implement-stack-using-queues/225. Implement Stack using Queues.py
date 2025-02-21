class MyStack:
    # [.     1 2 3 4.     ]  pop -> 4
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
        self.tops = 0
        

    def push(self, x: int) -> None:
        self.tops = x

        self.q1.append(x)
        

    def pop(self) -> int:
        for _ in range(len(self.q1) - 1):
            print(self.q1)
            self.q2.append(self.q1.popleft())
            print(self.q1)

        
        x = self.q1.pop()

        for _ in range(len(self.q2)):
            y = self.q2.popleft()
            self.q1.append(y)
            self.tops = y
        
        # self.top = self.q1[len(self.q1) - 1]

        return x

        

    def top(self) -> int:
        return self.tops
        

    def empty(self) -> bool:
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()