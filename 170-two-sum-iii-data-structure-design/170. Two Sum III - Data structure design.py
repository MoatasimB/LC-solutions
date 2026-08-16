class TwoSum:

    def __init__(self):
        self.lst = SortedList()

    def add(self, number: int) -> None:
        self.lst.add(number)

    def find(self, value: int) -> bool:
        l = 0
        r = len(self.lst) - 1

        while l < r:
            val = self.lst[l] + self.lst[r]
            if val < value:
                l += 1
            elif val > value:
                r -= 1
            elif val == value:
                return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)