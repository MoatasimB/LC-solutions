class SegTree:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.tree = [0] * (4 * self.n)
        self.leftCh = [""] * (4 * self.n)
        self.rightCh = [""] * (4 * self.n)
        self.pre = [0] * (4 * self.n)
        self.suf = [0] * (4 * self.n)

        self.build(1, 0, self.n - 1)

    def build(self, treeIdx, l, r):
        if l == r:
            self.leftCh[treeIdx] = self.s[l]
            self.rightCh[treeIdx] = self.s[l]
            self.tree[treeIdx] = 1
            self.pre[treeIdx] = 1
            self.suf[treeIdx] = 1
            return
        mid = (l + r) // 2
        left_idx = treeIdx * 2
        right_idx = treeIdx * 2 + 1

        self.build(left_idx, l, mid)
        self.build(right_idx, mid + 1, r)

        leftChild_rightCh = self.rightCh[left_idx]
        rightChild_leftCh = self.leftCh[right_idx]
        self.leftCh[treeIdx] = self.leftCh[left_idx]
        self.rightCh[treeIdx] = self.rightCh[right_idx]
        self.tree[treeIdx] = max(self.tree[left_idx], self.tree[right_idx])
        self.pre[treeIdx] = self.pre[left_idx]
        self.suf[treeIdx] = self.suf[right_idx]
        if leftChild_rightCh == rightChild_leftCh:
            leftChild_suf = self.suf[left_idx]
            rightChild_pre = self.pre[right_idx]
            self.tree[treeIdx] = max(self.tree[treeIdx], leftChild_suf +  rightChild_pre)
            #prefix
            if self.pre[left_idx] == mid - l + 1:
                self.pre[treeIdx] += rightChild_pre

            #suffix
            if self.suf[right_idx] == r - mid:
                self.suf[treeIdx] += leftChild_suf
    
    def update(self, treeIdx, l, r, newCh, idx):
        if l == r:
            self.leftCh[treeIdx] = newCh
            self.rightCh[treeIdx] = newCh
            return
        mid = (l + r) // 2
        left_idx = treeIdx * 2
        right_idx = treeIdx * 2 + 1

        if idx <= mid:
            self.update(left_idx, l, mid, newCh, idx)
        else:
            self.update(right_idx, mid + 1, r, newCh, idx)
        
        leftChild_rightCh = self.rightCh[left_idx]
        rightChild_leftCh = self.leftCh[right_idx]
        self.leftCh[treeIdx] = self.leftCh[left_idx]
        self.rightCh[treeIdx] = self.rightCh[right_idx]
        self.tree[treeIdx] = max(self.tree[left_idx], self.tree[right_idx])
        self.pre[treeIdx] = self.pre[left_idx]
        self.suf[treeIdx] = self.suf[right_idx]
        if leftChild_rightCh == rightChild_leftCh:
            leftChild_suf = self.suf[left_idx]
            rightChild_pre = self.pre[right_idx]
            self.tree[treeIdx] = max(self.tree[treeIdx], leftChild_suf +  rightChild_pre)
            
            #prefix
            if self.pre[left_idx] == mid - l + 1:
                self.pre[treeIdx] += rightChild_pre

            #suffix
            if self.suf[right_idx] == r - mid:
                self.suf[treeIdx] += leftChild_suf

    def query(self, treeIdx, l, r, ql, qr):
        if qr < l or ql > r:
            return float("-inf")

        if ql <= l <= r <= qr:
            return self.tree[treeIdx]
        
        mid = (l + r) // 2
        left_idx = treeIdx * 2
        right_idx = treeIdx * 2 + 1
        left = self.query(left_idx, l, mid, ql, qr)
        right = self.query(right_idx, mid + 1, r, ql, qr)
        return max(left, right)

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:

        segTree = SegTree(s)
        ans = []
        n = len(s)

        for idx, ch in zip(queryIndices, queryCharacters):
            segTree.update(1, 0, n - 1, ch, idx)
            ans.append(segTree.query(1, 0, n - 1, 0, n - 1))
        
        return ans

        