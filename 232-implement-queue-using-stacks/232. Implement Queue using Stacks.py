class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None
        

    def push(self, x: int) -> None:
        if not self.front:
            self.front = x
        
        self.stack1.append(x)
        

    def pop(self) -> int:
        if self.stack2:
            x = self.stack2.pop()
            if self.stack2:
                self.front = self.stack2[-1]
            elif not self.stack2 and self.stack1:
                self.front = self.stack1[0]
            else:
                self.front = None
            return x
        else:
        


            while self.stack1:
                self.stack2.append(self.stack1.pop())
            
            x = self.stack2.pop()
            if self.stack2:
                self.front = self.stack2[-1]
            elif not self.stack2 and self.stack1:
                self.front = self.stack1[0]
            else:
                self.front = None
            return x

        

    def peek(self) -> int:
        return self.front
        

    def empty(self) -> bool:
        return len(self.stack1) ==0 and len(self.stack2) ==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()