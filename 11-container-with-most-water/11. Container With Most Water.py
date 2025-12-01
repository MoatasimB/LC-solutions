class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        ans = 0

        l = 0
        r = len(height) - 1

        while l <= r:
            width = r - l
            h = min(height[r], height[l])

            ans = max(ans , width * h)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return ans