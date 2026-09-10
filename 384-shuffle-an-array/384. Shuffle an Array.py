class Solution:

    def __init__(self, nums: List[int]):
        self.curr = nums
        self.original = nums.copy()
        

    def reset(self) -> List[int]:
        self.curr = self.original.copy()
        return self.curr
        

    def shuffle(self) -> List[int]:
        
        for i in range(len(self.curr)):
            idx = random.randint(i, len(self.curr) - 1)
            self.curr[i], self.curr[idx] = self.curr[idx], self.curr[i]
        
        return self.curr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()