class SegmentTree:

    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.mins = [0] * (4 * self.n)
        self.maxs = [0] * (4 * self.n)
        self.build(1, 0 , self.n - 1)
    
    def build(self, node_idx, li, ri):
        if li == ri:
            self.mins[node_idx] = self.arr[li]
            self.maxs[node_idx] = self.arr[li]
            return
        
        mid = (li + ri) // 2
        left_child_idx = node_idx * 2
        right_child_idx = node_idx * 2 + 1

        self.build(left_child_idx, li, mid)
        self.build(right_child_idx, mid + 1, ri)

        self.mins[node_idx] = min(self.mins[left_child_idx], self.mins[right_child_idx])
        self.maxs[node_idx] = max(self.maxs[left_child_idx], self.maxs[right_child_idx])
    
    def queryMin(self, node_idx, li, ri, lr, rr):
        
        if lr > ri or rr < li:
            return float("inf")
        
        if lr <= li <= ri <= rr:
            return self.mins[node_idx]


        mid = (li + ri) // 2
        left_child_idx = node_idx * 2
        right_child_idx = node_idx * 2 + 1
        
        if rr <= mid:
            return self.queryMin(left_child_idx, li, mid, lr, rr)
        elif lr >= mid + 1:
            return self.queryMin(right_child_idx, mid + 1, ri, lr, rr)

        left_query = self.queryMin(left_child_idx, li, mid, lr, rr)
        right_query = self.queryMin(right_child_idx, mid + 1, ri, lr, rr)

        return min(left_query, right_query)


    
    def queryMax(self, node_idx, li, ri, lr, rr):
        if lr > ri or rr < li:
            return float("-inf")
        
        if lr <= li <= ri <= rr:
            return self.maxs[node_idx]


        mid = (li + ri) // 2
        left_child_idx = node_idx * 2
        right_child_idx = node_idx * 2 + 1
        if rr <= mid:
            return self.queryMax(left_child_idx, li, mid, lr, rr)
        elif lr >= mid + 1:
            return self.queryMax(right_child_idx, mid + 1, ri, lr, rr)
        
        left_query = self.queryMax(left_child_idx, li, mid, lr, rr)
        right_query = self.queryMax(right_child_idx, mid + 1, ri, lr, rr)

        return max(left_query, right_query)

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        segTree = SegmentTree(nums)
        n = len(nums)
        pq = []

        for l in range(n):
            minVal = segTree.queryMin(1, 0, n - 1, l, n - 1)
            maxVal = segTree.queryMax(1, 0, n - 1, l, n - 1)
            val = maxVal - minVal
            heapq.heappush(pq, [-val, l, n - 1])
        
        ans = 0
        while k:
            val, l, r = heapq.heappop(pq)
            ans -= val
            k -= 1

            if r > l:
                r -= 1
                minVal = segTree.queryMin(1, 0, n - 1, l, r)
                maxVal = segTree.queryMax(1, 0, n - 1, l, r)
                val = maxVal - minVal
                heapq.heappush(pq, [-val, l, r])
        
        return ans


        

        