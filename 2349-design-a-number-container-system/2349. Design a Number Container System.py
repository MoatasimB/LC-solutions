class NumberContainers:

    def __init__(self):
        self.idx_to_num = {}
        self.num_to_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        
        self.idx_to_num[index] = number
        
        heapq.heappush(self.num_to_indices[number], index)


    def find(self, number: int) -> int:
        if number not in self.num_to_indices or len(self.num_to_indices[number]) == 0:
            return -1

        while self.num_to_indices[number] and self.idx_to_num[self.num_to_indices[number][0]] != number:
            heapq.heappop(self.num_to_indices[number])
        return self.num_to_indices[number][0] if self.num_to_indices[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)