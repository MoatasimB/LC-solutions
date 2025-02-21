class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        for _ in range(len(self.q1)-1):
            self.q2.append(self.q1.popleft())
        
        x = self.q1.popleft()

        for _ in range(len(self.q2 )):
            self.q1.append(self.q2.popleft())
        
    

        return x
  
        

    def top(self) -> int:
        j = None
        for i in range(len(self.q1)):
            j = self.q1[i]
        
        return j

    def empty(self) -> bool:

        return len(self.q1) == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()