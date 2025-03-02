class Bitset:

    def __init__(self, size: int):
        self.bit = [0] * size
        self.size = size
        self.ones = 0
        self.flipp = False

    def fix(self, idx: int) -> None:
        if not self.flipp:
            if self.bit[idx] != 1:
                self.bit[idx] = 1
                self.ones +=1
        else:
            if self.bit[idx] == 1:
                self.bit[idx] = 0
                self.ones += 1

    def unfix(self, idx: int) -> None:
        if not self.flipp:
            if self.bit[idx] == 1:
                self.bit[idx] = 0
                self.ones -=1
        else:
            if self.bit[idx] == 0:
                self.bit[idx] = 1
                self.ones -= 1 

    def flip(self) -> None:
        self.flipp = not self.flipp
        zeros = self.size - self.ones
        self.ones = zeros
        

    def all(self) -> bool:
        return self.ones == self.size 

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        if not self.flipp:
            lst = [str(bit) for bit in self.bit]
        else:
            lst = [str(1 - bit) for bit in self.bit]

        return "".join(lst)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()