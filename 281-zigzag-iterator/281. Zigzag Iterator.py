class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.idx1 = 0
        self.v1 = v1
        self.v2 = v2
        self.idx2 = 0
        self.turn = 0

    def next(self) -> int:
        if self.turn == 1 and self.idx2 >= len(self.v2):
            self.turn = 0

        if self.turn == 0:
            if self.idx1 < len(self.v1):
                val = self.v1[self.idx1]
                self.idx1 += 1
                self.turn = 1
                return val
            else:
                self.turn = 1
        if self.turn == 1:
            if self.idx2 < len(self.v2):
                val = self.v2[self.idx2]
                self.idx2 += 1
                self.turn = 0
                return val
            else:
                self.turn = 0

    def hasNext(self) -> bool:
        return self.idx1 < len(self.v1) or self.idx2 < len(self.v2)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())