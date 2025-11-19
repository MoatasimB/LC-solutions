class Solution:

    def __init__(self, w: List[int]):
        self.w = w

        self.pre = [self.w[0]]
        for num in self.w[1:]:
            self.pre.append(self.pre[-1] + num)
        
    def pickIndex(self) -> int:
        rand = random.randint(1, self.pre[-1])
        
        l = 0
        r = len(self.pre) - 1
        ans = 0
        while l <= r:
            mid = (l + r) // 2

            if self.pre[mid] == rand:
                return mid
            elif self.pre[mid] < rand:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1

        return ans
        # [1, 4]



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()