class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        minHeap = []
        maxHeap = []

        l = 0
        ans = 0
        for r in range(n):
            heapq.heappush(minHeap, [nums[r], r])
            heapq.heappush(maxHeap, [-nums[r], r])

            # minVal = minHeap[0][0]
            # maxVal = -maxHeap[0][0]

            while maxHeap and minHeap and (-maxHeap[0][0] -  minHeap[0][0]) * (r - l + 1) > k:
                l += 1
                while minHeap and minHeap[0][1] < l:
                    heapq.heappop(minHeap)
                while maxHeap and maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)

            if maxHeap and minHeap and (-maxHeap[0][0] -  minHeap[0][0]) * (r - l + 1) <= k:
                ans += r - l + 1

        return ans
                
                


            