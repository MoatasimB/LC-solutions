class RandomizedSet:

    def __init__(self):
        self.mpp = {} #val : idx
        self.lst = []
        

    def insert(self, val: int) -> bool:
        if val in self.mpp:
            return False
        idx = len(self.lst)
        self.mpp[val] = idx
        self.lst.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.mpp:
            return False
        
        last_element = self.lst[-1]

        remove_element_idx = self.mpp[val]
        self.lst[remove_element_idx] = last_element
        self.mpp[last_element] = remove_element_idx
        del self.mpp[val]
        self.lst.pop()
        return True

        

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.lst) - 1)
        return self.lst[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()