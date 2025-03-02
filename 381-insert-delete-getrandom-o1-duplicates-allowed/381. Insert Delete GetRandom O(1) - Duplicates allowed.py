
class RandomizedCollection:

    def __init__(self):
        self.indices = defaultdict(set)
        self.lst = []
        

    def insert(self, val: int) -> bool:
        self.indices[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.indices[val]) == 1

        

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False
        idx_to_remove = self.indices[val].pop()
 
        last_val = self.lst[-1]
        last_idx = len(self.lst) - 1
        self.indices[last_val].add(idx_to_remove)
        self.indices[last_val].remove(last_idx)

        self.lst[idx_to_remove], self.lst[last_idx] = self.lst[last_idx], self.lst[idx_to_remove]

        self.lst.pop()

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()