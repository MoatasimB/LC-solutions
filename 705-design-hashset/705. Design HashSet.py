class MyHashSet:

    def __init__(self):
        self.lst = [None] * (10**6 + 1)
    
    def getHash(self, key):
        return key % (10**6)

    def add(self, key: int) -> None:
        idx  = self.getHash(key)
        self.lst[idx] = key
        

    def remove(self, key: int) -> None:
        idx  = self.getHash(key)
        self.lst[idx] = None

    def contains(self, key: int) -> bool:
        idx  = self.getHash(key)
        return self.lst[idx] == key
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)