class RandomizedSet:

    def __init__(self):
        self.mpp = {} #val : idx
        self.lst = []


    def insert(self, val: int) -> bool:
        if val in self.mpp:
            return False
        self.mpp[val] = len(self.lst)
        self.lst.append(val)
        
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mpp:
            return False
        idx_to_remove = self.mpp[val]
        n = len(self.lst)
        last_idx = n - 1
        last_val = self.lst[last_idx]

        self.lst[idx_to_remove] = self.lst[last_idx]
        self.mpp[last_val] = idx_to_remove

        self.lst.pop()
        del self.mpp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()