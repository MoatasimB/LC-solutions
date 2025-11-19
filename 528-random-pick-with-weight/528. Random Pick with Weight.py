class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.pre = [w[0]]
        for wt in w[1:]:
            self.pre.append(self.pre[-1] + wt)

        

    def pickIndex(self) -> int:
        val = random.randint(1, self.pre[-1])
        l = 0
        r = len(self.pre) - 1
        ans = None
        while l <= r:
            mid = (l + r) // 2

            if val <= self.pre[mid]:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
            
        
        return ans



#    3. 17 18 25

# 3/25 14/25 1/25 7/25

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# 0001111111111111123333333

