class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        

        s = []
        l = []
        ans = 0
        left = 0
        for r in range(len(nums)):

            heapq.heappush(s, (nums[r], r))
            heapq.heappush(l, (-nums[r], r))

            while abs(s[0][0] - (-l[0][0])) > limit:
                print(left)
                left = min(s[0][1], l[0][1]) + 1
                while s[0][1] < left:
                    heapq.heappop(s)
                while l[0][1] < left:
                    heapq.heappop(l)
            
            ans = max(ans, r - left + 1)
        return ans
