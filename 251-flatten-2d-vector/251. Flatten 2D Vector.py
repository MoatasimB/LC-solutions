class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.n = len(self.vec)
        self.row = 0
        self.idx = 0

    def next(self) -> int:
        self.update()
        val = self.vec[self.row][self.idx]
        self.idx += 1
        return val

        
    def update(self):
        while self.row < self.n and (len(self.vec[self.row]) == 0 or self.idx == len(self.vec[self.row])):
            self.row += 1
            self.idx = 0
    
    def hasNext(self) -> bool:       
        self.update()

        return self.row < self.n
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()