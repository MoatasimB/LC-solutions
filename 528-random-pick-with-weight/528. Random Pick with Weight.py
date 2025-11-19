class Solution:

    def __init__(self, w: List[int]):
        self.w = [w[0]]
        for i in range(1, len(w)):
            self.w.append(self.w[-1] + w[i])
        


    def pickIndex(self) -> int:
        l = 0
        r = len(self.w) - 1

        randNum = random.randint(1, self.w[-1])
        if randNum <= self.w[0]:
            return 0
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if self.w[mid] > randNum :
                r = mid - 1
            elif self.w[mid] < randNum:
                ans = mid
                l = mid + 1
            else:
                return mid
        
        return ans + 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


#  3 14 1 7

#  3/25 14/25 1/25 7/25

#  0 1. 2. 3
#  3 17 18 25


