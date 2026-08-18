class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self.buildTree(1, 0, self.n - 1)
    
    def buildTree(self, treeIdx, l, r):
        if l == r:
            self.tree[treeIdx] = self.arr[l]
            return self.arr[l]
        
        mid = (l + r) // 2
        leftChildIdx = treeIdx * 2
        rightChildIdx = treeIdx * 2 + 1

        left = self.buildTree(leftChildIdx, l, mid)
        right = self.buildTree(rightChildIdx, mid + 1, r)

        self.tree[treeIdx] = left + right
        return self.tree[treeIdx]
    

    def query(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)
    
    def _query(self, treeIdx, l, r, qLeft, qRight):
        
        if qLeft > r or qRight < l:
            return 0
        
        if qLeft <= l  <= r <= qRight:
            return self.tree[treeIdx]
        
        mid = (l + r) // 2
        leftChildIdx = treeIdx * 2
        rightChildIdx = treeIdx * 2 + 1

        left = self._query(leftChildIdx, l, mid, qLeft, qRight)
        right = self._query(rightChildIdx, mid + 1, r, qLeft, qRight)

        return left + right
    
    def update(self, idx, val):
        self._update(1, 0, self.n - 1, idx, val)
    
    def _update(self, treeIdx, l, r, idx, val):
        if l == r:
            self.tree[treeIdx] = val
            return
        
        mid = (l + r) // 2
        leftChildIdx = treeIdx * 2
        rightChildIdx = treeIdx * 2 + 1

        if idx <= mid:
            self._update(leftChildIdx, l, mid, idx, val)
        else:
            self._update(rightChildIdx, mid + 1, r, idx, val)
        
        self.tree[treeIdx] = self.tree[leftChildIdx] + self.tree[rightChildIdx]
                




class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.trees = {}
        for i, row in enumerate(matrix):
            self.trees[i] = SegTree(row)

    def update(self, row: int, col: int, val: int) -> None:
        segTree = self.trees[row]
        segTree.update(col, val)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for r in range(row1, row2 + 1):
            segTree = self.trees[r]
            val = segTree.query(col1, col2)
            ans += val
        
        return ans

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)