class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self.sqs = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
    
    def apply(self, treeIdx, l, r, val):
        length = r - l + 1
        self.sqs[treeIdx] += 2 * val * self.tree[treeIdx] + length * val * val
        self.tree[treeIdx] += val * length
        self.lazy[treeIdx] += val

    def push_down(self, treeIdx, l, r):
        if self.lazy[treeIdx] == 0 or l == r:
            return
        val = self.lazy[treeIdx]
        mid = (l + r) // 2
        left = treeIdx * 2
        right = treeIdx * 2 + 1
        self.apply(left, l, mid, val)
        self.apply(right, mid +1, r, val)
        self.lazy[treeIdx] = 0
        
        
    def update(self, treeIdx, l, r, ql, qr, val):

        if ql <= l <= r <= qr:
            self.apply(treeIdx, l, r, val)
            return
        if r < ql or qr < l:
            return
        self.push_down(treeIdx, l, r)

        mid = (l + r) //2
        left = treeIdx * 2
        right = treeIdx * 2 + 1
        self.update(left, l, mid, ql, qr, val)
        self.update(right, mid + 1, r, ql, qr, val)
        
        self.tree[treeIdx] = self.tree[left] + self.tree[right]
        self.sqs[treeIdx] = self.sqs[left] + self.sqs[right]




class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        mpp = {}
        MOD = 10**9 + 7

        segTree = SegTree(nums)
        ans = 0
        for i in range(n):
            last_idx = mpp[nums[i]] if nums[i] in mpp else -1

            segTree.update(1, 0, n - 1, last_idx + 1, i, 1)
            ans += segTree.sqs[1] % (MOD)
            mpp[nums[i]] = i
        
        return ans % MOD

