class Node:
    def __init__(self, k):
        self.pre = [0] * (k)
        self.mul = 0
class SegTree:
    def __init__(self, arr, k):
        self.arr = arr
        self.n = len(arr)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]        
        self.build(1, 0, self.n - 1)
    

    def build(self, treeIdx, l, r):
        if l == r:
            node = self.tree[treeIdx]
            node.pre[self.arr[l] % self.k] += 1
            node.mul = self.arr[l] % self.k
            return
        
        mid = (l + r) // 2
        leftChildIdx = treeIdx * 2
        rightChildIdx = treeIdx * 2 + 1

        self.build(leftChildIdx, l, mid)
        self.build(rightChildIdx, mid + 1, r)

        self.merge(treeIdx, leftChildIdx, rightChildIdx)

    def merge(self, treeIdx, leftChildIdx, rightChildIdx):
        node = self.tree[treeIdx]
        leftNode = self.tree[leftChildIdx]
        rightNode = self.tree[rightChildIdx]
        node.pre = leftNode.pre.copy()

        for i in range(self.k):
            node.pre[(leftNode.mul * i) % self.k] += rightNode.pre[i]
        node.mul = (leftNode.mul * rightNode.mul) % self.k
    
    def update(self, treeIdx, l, r, idx, value):
        if l == r:
            node = self.tree[treeIdx]
            node.pre = [0] * self.k
            node.pre[value % self.k] += 1
            node.mul = value % self.k
            return
        mid = (l + r) // 2
        leftChildIdx = treeIdx * 2
        rightChildIdx = treeIdx * 2 + 1

        if idx <= mid:
            self.update(leftChildIdx, l, mid, idx, value)
        else:
            self.update(rightChildIdx, mid + 1, r, idx, value)
        
        self.merge(treeIdx, leftChildIdx, rightChildIdx)
    

    def query(self, treeIdx, l, r, ql, qr):

        if ql <= l <= r <= qr:
            node = self.tree[treeIdx]
            return [node.pre, node.mul]
        
        if l > qr or r < ql:
            return [None, None]

        mid = (l + r) // 2
        leftChildIdx = treeIdx * 2
        rightChildIdx = treeIdx * 2 + 1

        left_pre, left_mul = self.query(leftChildIdx, l, mid, ql, qr)
        right_pre, right_mul = self.query(rightChildIdx, mid + 1, r, ql, qr)

        if not left_pre:
            return [right_pre, right_mul]
        if not right_pre:
            return [left_pre, left_mul]
        
        pre = left_pre.copy()
        for i in range(self.k):
            pre[(left_mul * i) % self.k] += right_pre[i]
        mul = (left_mul * right_mul) % self.k
        return [pre, mul]







class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        
        segTree = SegTree(nums, k)
        n = len(nums)
        ans = []

        for idx, val, start, x_i in queries:
            segTree.update(1, 0, n - 1, idx, val)
            pre, mul = segTree.query(1, 0, n - 1, start, n - 1)
            ans.append(pre[x_i])
        return ans