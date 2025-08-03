class RandomizedSet:

    def __init__(self):
        self.l = []
        self.mpp = {} #val : idx
        

    def insert(self, val: int) -> bool:
        if val in self.mpp:
            return False
        
        self.mpp[val] = len(self.l)
        self.l.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.mpp:
            return False
        last_val = self.l[-1]
        val_idx = self.mpp[val]
        last_idx = self.mpp[last_val]

        self.l[val_idx], self.l[last_idx] = self.l[last_idx], self.l[val_idx]

        self.mpp[last_val] = val_idx
        del self.mpp[val]

        self.l.pop()
        return True

    def getRandom(self) -> int:
        idx = random.randint(0,len(self.l) - 1)
        return self.l[idx]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()