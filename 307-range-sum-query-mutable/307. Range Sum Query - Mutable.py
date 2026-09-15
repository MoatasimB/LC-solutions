class BitTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (self.n + 1)

        for i, val in enumerate(self.arr):
            self.update(i, val)
        print(self.tree)
    def update(self, i, val):

        i += 1
        while i <= self.n:
            self.tree[i] += val
            i += i & (-i)
    
    def prefix(self, i):
        i += 1
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= i & (-i)
        return ans
    
    def query(self, l, r):
        if l == 0:
            return self.prefix(r)
        
        return self.prefix(r) - self.prefix(l - 1)



class NumArray:

    def __init__(self, nums: List[int]):
        self.bitTree = BitTree(nums)
        self.nums = nums
        

    def update(self, index: int, val: int) -> None:
        original = self.nums[index]
        delta = val - original
        self.nums[index] = val
        self.bitTree.update(index, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self.bitTree.query(left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)