class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.indices = [0] * 2
        self.idxPtr = 0
        self.v1 = v1
        self.v2 = v2
        self.n1 = len(self.v1)
        self.n2 = len(self.v2)
        

    def next(self) -> int:
        
        if self.idxPtr == 0:
            idx1 = self.indices[self.idxPtr]
            if idx1 < self.n1:
                val = self.v1[idx1]
                self.indices[self.idxPtr] += 1
                self.idxPtr = (self.idxPtr + 1 )% 2
                return val
            else:
                self.idxPtr = 1
                return self.next()
        else:
            idx2 = self.indices[self.idxPtr]
            if idx2 < self.n2:
                val = self.v2[idx2]
                self.indices[self.idxPtr] += 1
                self.idxPtr = (self.idxPtr + 1 )% 2
                return val
            else:
                self.idxPtr = 0
                return self.next()
        



    def hasNext(self) -> bool:
        return sum(self.indices) < self.n1 + self.n2

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())