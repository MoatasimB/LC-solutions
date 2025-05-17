class Solution:

    def __init__(self, nums: List[int]):
        self.og = nums
        self.curr = nums
        

    def reset(self) -> List[int]:
        self.curr = self.og
        return self.curr

    def shuffle(self) -> List[int]:
        seen = set()
        ans = []
        while len(ans) != len(self.og):
            idx = random.randint(0,len(self.og)-1)
            while idx in seen:
                idx = random.randint(0,len(self.og)-1)
            
            ans.append(self.og[idx])
            seen.add(idx)

        return ans



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()