class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self.buildTree(1, 0, self.n - 1)
    
    def buildTree(self, node_idx, left_idx, right_idx):
        if left_idx == right_idx:
            self.tree[node_idx] = self.arr[left_idx]
            return
        
        mid = (left_idx + right_idx) // 2
        left_child_idx = node_idx * 2
        right_child_idx = node_idx * 2 + 1
        self.buildTree(left_child_idx, left_idx, mid)
        self.buildTree(right_child_idx, mid + 1, right_idx)

        self.tree[node_idx] = self.tree[left_child_idx] + self.tree[right_child_idx]
    
    def update(self, idx, val):
        self._update(1, 0, self.n - 1, idx, val)
    def _update(self, node_idx, left_idx, right_idx, idx, val):
        if left_idx == right_idx:
            self.tree[node_idx] += val
            return
        mid = (left_idx + right_idx) // 2
        left_child_idx = node_idx * 2
        right_child_idx = node_idx * 2 + 1
        if idx <= mid:
            self._update(left_child_idx, left_idx, mid, idx, val)
        else:
            self._update(right_child_idx, mid + 1, right_idx, idx, val)
        
        self.tree[node_idx] = self.tree[left_child_idx] + self.tree[right_child_idx]
    
    def rangeQuery(self, left, right):
        return self._findRangeQuery(1, 0, self.n - 1, left, right)
    
    def _findRangeQuery(self, node_idx, left_idx, right_idx, range_left, range_right):
        if range_right < left_idx or range_left > right_idx:
            return 0
        
        if range_left <= left_idx <= right_idx <= range_right:
            return self.tree[node_idx]
        
        mid = (left_idx + right_idx) // 2
        left_child_idx = node_idx * 2
        right_child_idx = node_idx * 2 + 1

        if range_right <= mid:
            return self._findRangeQuery(left_child_idx, left_idx, mid, range_left, range_right)
        elif mid < range_left:
            return self._findRangeQuery(right_child_idx, mid + 1, right_idx, range_left, range_right)

        left = self._findRangeQuery(left_child_idx, left_idx, mid, range_left, range_right)
        right = self._findRangeQuery(right_child_idx, mid + 1, right_idx, range_left, range_right)
        return left + right
    



class NumArray:

    def __init__(self, nums: List[int]):
        self.SegTree = SegTree(nums)
        self.nums = nums
        

    def update(self, index: int, val: int) -> None:
        curr = self.nums[index]
        diff = val - curr
        self.nums[index] = val
        self.SegTree.update(index, diff)

        

    def sumRange(self, left: int, right: int) -> int:
        return self.SegTree.rangeQuery(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)