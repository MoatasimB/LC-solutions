class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        if self.n:
            self.build(1, 0, self.n - 1)
    
    def build(self, nodeIdx, sr, er):
        if sr == er:
            self.tree[nodeIdx] = self.arr[sr]
            return
        
        mid = (sr + er) // 2
        leftChildIdx = nodeIdx * 2
        rightChildIdx = nodeIdx * 2 + 1

        self.build(leftChildIdx, sr, mid)
        self.build(rightChildIdx, mid + 1, er)
        self.tree[nodeIdx] = max(self.tree[leftChildIdx], self.tree[rightChildIdx])
    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, nodeIdx, sr, er, qs, qe):

        if er < qs or sr > qe:
            return float("-inf")
        
        if qs <= sr <= er <= qe:
            return self.tree[nodeIdx]

        mid = (sr + er) // 2
        leftChildIdx = nodeIdx * 2
        rightChildIdx = nodeIdx * 2 + 1

        left = self._query(leftChildIdx, sr, mid, qs, qe)
        right = self._query(rightChildIdx, mid + 1, er, qs, qe)

        return max(left, right)


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        
        n = len(s)
        oneCount = s.count("1")
        zeroBlocks = []
        blockStartIdx = []
        blockEndIdx = []

        i = 0

        while i < n:
            start = i

            while i < n and s[i] == s[start]:
                i += 1
            
            if s[start] == "0":
                zeroBlocks.append(i - start)
                blockStartIdx.append(start)
                blockEndIdx.append(i - 1)
        m = len(zeroBlocks)
        consecutiveBlocks = [zeroBlocks[i] + zeroBlocks[i + 1] 
        for i in range(m - 1)]

        segTree = SegmentTree(consecutiveBlocks)

        #blocks end = [3 , 7, 10, 12] Q = [4, 11] smallest value greater than l

        #blocks start = [0, 5, 9, 12] Q = [4, 11] largest value less than 11 


        def findStart(val, arr):
            n = len(arr)
            l = 0
            r = n - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2

                if arr[mid] == val:
                    return mid
                elif arr[mid] > val:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
        def findEnd(val, arr):
            n = len(arr)
            l = 0
            r = n - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2

                if arr[mid] == val:
                    return mid
                elif arr[mid] < val:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans

        
        if m < 2:
            return [oneCount] * len(queries)
        
        final = []
        for left, right in queries:
            print(left, right)
            idxStart = findStart(left, blockEndIdx)
            idxEnd = findEnd(right, blockStartIdx)

            if idxStart == -1 or idxEnd == -1 or idxStart >= idxEnd:
                final.append(oneCount)
                continue
            
            beginningZeros = blockEndIdx[idxStart] - max(left, blockStartIdx[idxStart]) + 1

            endingZeros = min(blockEndIdx[idxEnd], right) - blockStartIdx[idxEnd] + 1

            if idxStart + 1 == idxEnd:
                final.append(oneCount + beginningZeros + endingZeros)
                continue

            firstBlock = beginningZeros + zeroBlocks[idxStart + 1]
            middleBlock = segTree.query(idxStart + 1, idxEnd - 2)

            endBlock = endingZeros + zeroBlocks[idxEnd - 1]
            best = max(firstBlock, middleBlock, endBlock)
            final.append(oneCount + best)


        return final

