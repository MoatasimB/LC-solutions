class Logger:

    def __init__(self):
        self.next = {} #message: next time
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.next:
            self.next[message] = timestamp + 10
            return True

        time = self.next[message]
        if time > timestamp:
            return False

        self.next[message] = timestamp + 10
        return True            
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)