class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.q = deque()
        if v1:
            self.q.append([v1, 0])
        if v2:
            self.q.append([v2,0])

    def next(self) -> int:
        lst, idx = self.q.popleft()
        val = lst[idx]
        idx += 1
        if idx != len(lst):
            self.q.append([lst, idx])
        return val
            
        
    def hasNext(self) -> bool:
        return len(self.q) != 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())