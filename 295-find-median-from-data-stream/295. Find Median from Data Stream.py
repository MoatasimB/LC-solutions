class MedianFinder:

    def __init__(self):
        self.left = [] #maxHeap
        self.right = [] #minHeap
        


    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        if self.left and self.right and abs(self.left[0]) > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        
        if len(self.right) > len(self.left):
            val = -heapq.heappop(self.right)
            heapq.heappush(self.left, val)

    def findMedian(self) -> float:
        total = len(self.left) + len(self.right)

        if total % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()