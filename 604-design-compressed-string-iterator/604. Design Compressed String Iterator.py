class StringIterator:

    def __init__(self, compressedString: str):
        self.idx = 0
        self.count = 0
        self.s = compressedString
        self.nextIdx = -1
        self.getCount()
    
    def getCount(self):
        start = self.idx + 1
        self.count = 0
        while start < len(self.s) and self.s[start].isdigit():
            self.count = self.count * 10 + int(self.s[start])
            start += 1
        self.nextIdx = start
        

    def next(self) -> str:
        if not self.hasNext():
            return " "
        ch = self.s[self.idx]
        self.count -= 1
        if self.count == 0:
            self.idx = self.nextIdx
            self.getCount()

        return ch
        

    def hasNext(self) -> bool:
        return self.count > 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()