class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self.buildTree(1, 0, self.n - 1)
    
    def getChildren(self, nodeIdx, l, r):
        mid = (l + r) // 2
        leftChild = nodeIdx * 2
        rightChild = nodeIdx * 2 + 1
        return [leftChild, rightChild, mid]

    def buildTree(self, nodeIdx, l, r):
        if l == r:
            self.tree[nodeIdx] = self.arr[l]
            return self.tree[nodeIdx]
        
        leftChild, rightChild, mid = self.getChildren(nodeIdx, l, r)

        left = self.buildTree(leftChild, l, mid)
        right = self.buildTree(rightChild, mid + 1, r)

        self.tree[nodeIdx] = left + right
        return self.tree[nodeIdx]
    
    def update(self, idx, val):
        return self._update(1, 0, self.n - 1, idx, val)
    
    def _update(self, nodeIdx, l, r, idx, val):
        if l == r:
            self.tree[nodeIdx] = val
            return
        
        leftChild, rightChild, mid = self.getChildren(nodeIdx, l, r)

        if idx <= mid:
            self._update(leftChild, l, mid, idx, val)
        else:
            self._update(rightChild, mid + 1, r, idx, val)
        
        left = self.tree[leftChild]
        right = self.tree[rightChild]

        self.tree[nodeIdx] = left + right
    
    def query(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)
    
    def _query(self, nodeIdx, l, r, ql, qr):

        if qr < l or ql > r:
            return 0
        
        if ql <= l <= r <= qr:
            return self.tree[nodeIdx]
        
        leftChild, rightChild, mid = self.getChildren(nodeIdx, l, r)

        return self._query(leftChild, l, mid, ql, qr) + self._query(rightChild, mid + 1, r, ql, qr)






class NumArray:

    def __init__(self, nums: List[int]):
        self.segTree = SegTree(nums)
        

    def update(self, index: int, val: int) -> None:
        self.segTree.update(index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.segTree.query(left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)