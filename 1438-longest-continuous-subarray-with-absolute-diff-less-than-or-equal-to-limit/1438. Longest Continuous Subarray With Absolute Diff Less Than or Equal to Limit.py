class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        

        minH = []
        maxH = []

        l = 0
        ans = 0
        for r in range(len(nums)):

            heapq.heappush(minH, (nums[r], r))
            heapq.heappush(maxH, (-nums[r], r))

            while abs(-maxH[0][0] - minH[0][0]) > limit:
                l = min(maxH[0][1], minH[0][1])
                while minH[0][1] <= l:
                    heapq.heappop(minH)
                while maxH[0][1] <= l:
                    heapq.heappop(maxH)
                l += 1
            ans = max(ans, abs(r - l) + 1)
        
        return ans

