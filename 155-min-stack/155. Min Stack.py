class MinStack:

    def __init__(self):
        self.s1 = []
        # self.s2 = [] 

    def push(self, val: int) -> None:
        if self.s1:
            self.s1.append([val, min(val, self.s1[-1][1])])
        else:
            self.s1.append([val,val])


    def pop(self) -> None:
        self.s1.pop()
        

    def top(self) -> int:
        return self.s1[-1][0]
        

    def getMin(self) -> int:
        return self.s1[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()