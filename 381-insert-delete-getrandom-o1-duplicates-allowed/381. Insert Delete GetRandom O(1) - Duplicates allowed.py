class RandomizedCollection:

    def __init__(self):
        self.mpp = defaultdict(set) #val = [set]
        self.lst = []
        

    def insert(self, val: int) -> bool:
        is_not_in = True
        if val in self.mpp and len(self.mpp[val]) != 0:
            is_not_in = False
        idx = len(self.lst)
        self.mpp[val].add(idx)
        self.lst.append(val)
        return is_not_in

    # [1, 3, 2, 3, 3]
    def remove(self, val: int) -> bool:
        if val not in self.mpp or len(self.mpp[val]) == 0:
            return False
        last_elem = self.lst[-1]
        remove_idx = self.mpp[val].pop()

        self.mpp[last_elem].add(remove_idx)
        self.mpp[last_elem].remove(len(self.lst) - 1)

        self.lst[remove_idx] = last_elem
        self.lst.pop()

        return True

        

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()