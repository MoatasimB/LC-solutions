class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        indexOfElement = self.map[val]
        n = len(self.arr)
        lastElement = self.arr[n - 1]

        self.arr[indexOfElement] = lastElement
        self.arr.pop()
        self.map[lastElement] = indexOfElement
        del self.map[val]
        return True
        

    def getRandom(self) -> int:
        n = random.randint(0, len(self.arr) - 1)
        return self.arr[n]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()