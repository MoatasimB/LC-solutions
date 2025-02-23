class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1 = nums1
        self.n2 = nums2
        self.idx_num = {}
        self.num_counts = defaultdict(int)

        for i in range(len(self.n2)):
            self.idx_num[i] = self.n2[i]
            self.num_counts[self.n2[i]] += 1


    def add(self, index: int, val: int) -> None:
        num = self.idx_num[index]
        self.num_counts[num] -= 1
        if self.num_counts[num] == 0:
            del self.num_counts[num]
        self.idx_num[index] = num + val
        self.num_counts[num + val] += 1
    
    def count(self, tot: int) -> int:
        ans = 0
        for i in range(len(self.n1)):
            if (tot - self.n1[i]) in self.num_counts:
                ans += self.num_counts[tot - self.n1[i]]
        
        return ans